import openai
import os
import pandas as pd
import numpy as np
import configparser
from getpass import getpass
from openai.embeddings_utils import get_embedding
from llama_index import GPTSimpleVectorIndex

# Read config
config = configparser.ConfigParser()
config.read('config.ini')

# Write KEY for openAI API
os.environ['OPENAI_API_KEY'] = config['openai']['api_key']

# Load you data into 'Documents' a custom type by LlamaIndex

from llama_index import SimpleDirectoryReader

documents = SimpleDirectoryReader('./custom-knowledge-chatbot/data').load_data()

index = GPTSimpleVectorIndex.from_documents(documents)

# Query your index!

response = index.query("Con qué resolución puedo escanearme en 3D los cojones con un Photoneo? En plan, qué resolución mínima y máxima puedo tener en el 3D de mis cojones?")
print("Con qué resolución puedo escanearme en 3D los cojones con un Photoneo? En plan, qué resolución mínima y máxima puedo tener en el 3D de mis cojones?")
print(response)