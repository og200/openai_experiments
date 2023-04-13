# Vector Database Experiment

This is a simple experiment using a vector database. 

The aim of this experiment is to show one simple way that GPT can be deployed
to respond to prompts that depend on a large set of proprietary textual fragments.

This could, in its simplest form, be used to ingest a set of documentation and
answer questions about the concepts described in the documentation using
GPT.

The implementation has two parts:

## Build

This will ingest a set of text fragments, convert them to vector embeddings 
using OpenAI, then ingest them into a Pinecone vector database.

## Run

This will take a prompt, create a vector embedding from the prompt using OpenAI,
search the Pinecone database to find relevant text fragments. It then passes
those embedded fragments to OpenAI along with the initial prompt and prints the results.


# Setting up
1. Ensure you have Python 3.10 or newer installed. We would recommend having a Python virutal enviroment set up
   and working within that.
2. Check the openai_experiemnts repository out using git
3. Run pip install -e <path to the repo you checked out>

# Configuration

1. Copy config_template.py as config.py
2. Put your openai and pinecone api keys into config.py

# Usage

Run build.py to create the initial vector database. This will load sample data
into the database after embedding each text chunk.

Run run.py to run prompts against the database.




