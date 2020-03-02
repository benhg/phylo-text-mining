import regex as re
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
	tail_regex = r"([a-zA-Z0-9])\1{3,}"
	all_matches = re.match(sequence)
	for match in all_matches:
		sequence.replace(match, "")

	return sequence


