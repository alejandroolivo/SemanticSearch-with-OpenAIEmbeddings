import os
import csv
import xml.etree.ElementTree as ET

# Define the root directory path
rootdir = 'K:\Contenido Catalogo'

# Create an empty list to store the tags
tagsList = []

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

                # Add tags to the tags list
                for tag in tags:
                    tagsList.append(tag.strip().replace(' ', '-'))

# Sort the tags list
tagsList.sort()


# Export the tags list to a CSV file, removing duplicates
with open('.\Data\Tags.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(['tag'])
    for item in sorted(set(tagsList)):
        writer.writerow([item])