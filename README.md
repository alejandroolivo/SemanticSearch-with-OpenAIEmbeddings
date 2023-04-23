# SemanticSearch-with-OpenAIEmbeddings
This project consists of six Python scripts that perform various tasks related to natural language processing (NLP) and semantic search. The scripts use openAI API to obtain word embeddings and calculate cosine similarity to perform semantic search. The project aims to extract tags from XML files, calculate word embeddings for tags, and perform semantic search on the tags.

## Installation
To run the scripts, you need to have Python 3 installed on your machine. You can download Python from the official website. Additionally, you need to install the following Python packages:

- openai
- pandas
- numpy
- configparser
- getpass
- xml.etree.ElementTree
- csv
- llama_index

You can install these packages using the following command:

  `pip install openai pandas numpy configparser getpass llama_index`
  
## Script Description
1. ExtractTags.py
This script extracts tags from XML files located in a directory and saves them to a CSV file. The script uses the xml.etree.ElementTree module to parse the XML files and extract the tags. The tags are then cleaned, sorted, and saved to a CSV file.

2. SemanticSearch.py
This script performs semantic search on a CSV file containing word embeddings of tags. The script prompts the user to enter a search term, calculates the cosine similarity between the search term and each tag, sorts the tags by similarity, and saves the results to a CSV file.

3. CreateEmbeddings.py
This script creates word embeddings for the tags extracted in ExtractTags.py. The script uses the openAI API to generate word embeddings for each tag and saves them to a CSV file.

4. LlamaTest.py
This script demonstrates the usage of the llama_index package for performing semantic search. The script loads a directory of text documents, creates a GPT-based vector index for the documents, and queries the index for a given search term.

5. config.ini
This file contains the openAI API key that is used by the scripts.

6. Data Directory
This directory contains the CSV files generated by the scripts.

## Usage
To use the scripts, follow these steps:

1. Clone the repository to your local machine.
2. Install the required packages using the pip command mentioned above.
3. Obtain an openAI API key and add it to the config.ini file.
4. Run the scripts in the following order:

  - python ExtractTags.py
  
  - python CreateEmbeddings.py
  
  - python SemanticSearch.py
  
  - python TestScript.py

5. The generated CSV files can be found in the Data directory.

## Conclusion
This project provides a simple demonstration of how to perform semantic search using openAI API and Python. The project can be extended to handle large-scale text datasets and more complex NLP tasks.

## License
This project is licensed under the Apache License 2.0. For more information, please refer to the [LICENSE](LICENSE) file in the root of this repository.
