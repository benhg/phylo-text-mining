import regex as re
import string
from Bio import SeqIO
import sys
"""
Stopping and Stemming should help us
reduce the data closer to purely semantic units.

There are several types of things that this entails
This module should help to filter out our equivalent of "stop-words"
"""

def remove_long_tails(sequence):
	"""
	One of the more frequent issues that shows up with data like this
	is repeated subsequences - ie `eeeeeee` or `kkkkkkk` in sequence
	"""
	tail_regex = r"(\w)\2+"
	all_matches = re.findall(tail_regex, sequence)
	for match in all_matches:
		print(match)
		sequence = sequence.replace(match, "")

	return sequence

def remove_long_tails_no_regex(sequence):
	"""
	Do the same as above, but no regex
	"""
	letters = list(string.ascii_uppercase + string.ascii_lowercase)
	for letter in letters:
		for i in range(10, 4, -1):
			letter_pattern = letter*i
			if letter_pattern in sequence:
				sequence = sequence.replace(letter_pattern, "")
	return sequence



def fully_stem_and_lemmatize(sequence):
	"""
	Run all of the stemming/lemmatizing in a row
	"""
	sequence = remove_long_tails_no_regex(sequence)
	return sequence

def stem_and_lemmatize_in_fasta_file(fasta_file_location, output_file_location):
	with open(output_file_location, "w") as fh:
		for record in SeqIO.parse(handle, "fasta"):
                fh.write(f">{record.id}\n")
                fh.write(str(fully_stem_and_lemmatize(str(record.seq))))



if __name__ == '__main__':
	if len(sys.argv) != 3:
		print(f"Usage: {sys.argv[0]} <Input file> <Output file>")
		exit(1)

	stem_and_lemmatize_in_fasta_file(sys.argv[1] sys.argv[2])
