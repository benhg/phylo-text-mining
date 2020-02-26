from glob import glob
import os
import sys
from nltk.tokenize import RegexpTokenizer

"""
Basic first-pass at an LDA

Just does the super simple boring LDA on the input dir you give it
"""

def load_documents(input_dir):
	documents = []
	filenames = glob(f"{input_dir}/*.txt")
	for filename in filenames:
		with open(filename) as fh:
			documents.append(fh.read())
	return documents

def tokenize_docs(docs):
	# Split the documents into tokens.
	tokenizer = RegexpTokenizer(r'\w+')
	for idx in range(len(docs)):
    	docs[idx] = docs[idx].lower()  # Convert to lowercase.
    	docs[idx] = tokenizer.tokenize(docs[idx])  # Split into words.

	# Remove numbers, but not words that contain numbers.
	docs = [[token for token in doc if not token.isnumeric()] for doc in docs]

	# Remove words that are only one character.
	docs = [[token for token in doc if len(token) > 1] for doc in docs]
	return docs


if __name__ == '__main__':
	if not ( 2 == len(sys.argv)):
		print("Usage: python3 basic_lda.py <input_dir>")
		exit(1)

	input_dir = sys.argv[1]
	if not os.path.isdir(input_dir):
		print("Input Dir Does Not Exist")
		exit(1)
	species = sys.argv[1]
	documents = load_documents(input_dir)
	tokenized_docs = tokenized_docs(documents)
	print(tokenized_docs)