from glob import glob
import os
import sys

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
	print(documents)