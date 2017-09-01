"""This module does blah blah."""
import xml.etree.ElementTree
import unicodecsv as csv
import re
import sys
import os

for f in sys.argv[1:]:
    fileLoc = os.path.splitext(f)[0]
    # Open the file and strip out unnecessary data that might give errors.
    with open(f, 'r') as myFile:
        fileText = re.sub("<head>.*?</head>", "", myFile.read(), flags=re.DOTALL)
        fileText = re.sub("<meta.*?>", "", fileText, flags=re.DOTALL)

    # Parse the XML (HTML) in the file.
    yfirlit = xml.etree.ElementTree.fromstring(fileText)

    # Open a CSV file to write to.
    with open(fileLoc + '.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=";")

        # Find all entries
        for faersla in yfirlit.find("body").find("table"):
            myList = []
            for faersluhlutur in faersla:
                if faersluhlutur.text is None:
                    myList.append("")
                else:
                    myList.append(faersluhlutur.text)
            writer.writerow(myList)
