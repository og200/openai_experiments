"""
This code extracts text from a Gmail dump created by Google TakeOut

We use it to read an entire email mailbox, including attachements, as text so we can then move the content into
a vector database for further processing.
"""


### TODO ###
### Switch to unstructured-io (https://github.com/Unstructured-IO)

from pathlib import Path
import mailbox
import email
import os
import io
import base64

from bs4 import BeautifulSoup
import PyPDF2
import docx


from openai_experiments import config
import openai_experiments
from openai_experiments.log import log
import pinceone


mbox_file = Path('~/Downloads/Takeout/Mail/All mail Including Spam and Trash.mbox')

metadata_config = dict(
    indexed=['from', 'to', 'date']
)

pinceone.init(api_key=config.pinecone_api_key, environment=config.pinecone_environment)
pinecone.create_index(name="email", dimensions=512, metadata_config=metadata_config)
index = pinecone.Index("email")


def extract_plain_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()


def extract_plain_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


def extract_plain_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text


def extract_plain_text_from_email(msg):
    content_type = msg.get_content_type()
    if content_type == 'text/plain':
        return msg.get_payload(decode=True).decode(errors='ignore')
    elif content_type == 'text/html':
        return extract_plain_text_from_html(msg.get_payload(decode=True).decode(errors='ignore'))
    elif content_type == 'multipart/alternative' or content_type == 'multipart/mixed':
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                return part.get_payload(decode=True).decode(errors='ignore')
            elif part.get_content_type() == 'text/html':
                return extract_plain_text_from_html(part.get_payload(decode=True).decode(errors='ignore'))
    return None


def process_attachments(msg, output_dir):
    for part in msg.walk():
        content_disposition = part.get('Content-Disposition', '')
        if 'attachment' in content_disposition:
            filename = part.get_filename()

            if not filename:
                continue

            file_data = part.get_payload(decode=True)

            f = io.BytesIO(file_data)
            if filename.endswith('.pdf'):
                print('='*80)
                print(f' PDF: {filename}')
                print('-'*80)
                print(extract_plain_text_from_pdf(f))
                print('-'*80)

            elif filename.endswith('.docx'):
                print('='*80)
                print(f' DOCX: {filename}')
                print('-'*80)
                print(extract_plain_text_from_docx(f))
                print('-'*80)


def extract_texts_from_mbox(mbox_file, output_dir='attachments'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    mbox = mailbox.mbox(mbox_file)
    for msg in mbox:
        plain_text = extract_plain_text_from_email(msg)
        print('=' * 80)
        print('=' * 80)
        print(' MESSAGE')
        print('-' * 80)
        if plain_text:
            print(plain_text)
        process_attachments(msg, output_dir)
        print('=' * 80)
        print('=' * 80)

if __name__ == "__main__":
    extract_texts_from_mbox(mbox_file)