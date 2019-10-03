""" Brief spacy demo.

Runs standard spacy processor on text from
stdin and displays it with spacy.

Usage python3 spacy-demo.py < path/to/input

"""

import sys
import spacy
from spacy import displacy


# load a model
nlp = spacy.load("en_core_web_sm")

# load a file to process
# with open('path/to/file', 'r') as reader:
#     text = reader.read()

text = sys.stdin.read()

# process the text
doc = nlp(text)

# view the entities
displacy.serve(doc, style="ent")
