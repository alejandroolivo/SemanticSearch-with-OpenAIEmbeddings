import os
import configparser
from llama_index import GPTSimpleVectorIndex

# Read config
config = configparser.ConfigParser()
config.read('config.ini')

# Write KEY for openAI API
os.environ['OPENAI_API_KEY'] = config['openai']['api_key']

# Load you data into 'Documents' a custom type by LlamaIndex

from llama_index import SimpleDirectoryReader

documents = SimpleDirectoryReader('./Data/LlamaTestChunk').load_data()

index = GPTSimpleVectorIndex.from_documents(documents)

# Query your index!

pregunta = "Con qué resolución puedo escanearme en 3D los cojones con un Photoneo? En plan, qué resolución mínima y máxima puedo tener en el 3D de mis cojones?"

response = index.query(pregunta)
print(pregunta)
print(response)