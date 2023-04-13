"""
Build the vector database we will later use for retrieving text chunks to feed to OpenAI
"""

import time

import pinecone
import openai

