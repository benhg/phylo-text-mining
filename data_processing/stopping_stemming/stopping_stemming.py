import regex as re
import string
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


if __name__ == '__main__':
	sequence = "AAAAAKKKKKCCCKDEKCAOCDASCPWSZJU"
	print(fully_stem_and_lemmatize(sequence))