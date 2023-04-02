import os
import csv
import xml.etree.ElementTree as ET

# Define the root directory path
rootdir = 'K:\Contenido Catalogo'

# Create an empty set to store the tags
tagsSet = set()

# Iterate over each file and directory inside the root directory
for subdir, dirs, files in os.walk(rootdir):
    for file in files:

        # Check if the file is an XML file
        if file.endswith('.xml') and not file.startswith('Logs'):

            # Combine the directory path and file name to get the full file path
            filepath = os.path.join(subdir, file)

            # Parse the XML file
            tree = ET.parse(filepath)
            root = tree.getroot()

            # Check if the "Tags" element exists in the XML file
            tagsElem = root.find('Tags')
            if tagsElem is not None and tagsElem.text is not None:
                tags = tagsElem.text.split(',')

                # Add tags to the tags set
                for tag in tags:
                    tagsSet.add(tag.strip().replace(' ', '-'))

# Sort the tags set
tagsList = sorted(tagsSet)

# Remove duplicates from the tagsList
tagsList = list(set(tagsList))

# Batch size
BATCH_SIZE = 20

# Clear the output directory
for file in os.listdir('.\Data\Tags Batches'):
    os.remove(os.path.join('.\Data\Tags Batches', file))

# Export the tags to multiple CSV files, one per batch
for i in range(0, len(tagsList), BATCH_SIZE):
    batch = tagsList[i:i + BATCH_SIZE]
    filename = f".\Data\Tags Batches\Tags_batch{i//BATCH_SIZE+1}.csv"
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(['tag'])
        for tag in batch:
            writer.writerow([tag])
