from Bio import SeqIO

import sys
import os
"""
Generate words as chunks of proteins.

Use a sliding window to create a "minimum semantic unit"

For a single transcript, treat each sequence as a document.
"""

SLIDING_WINDOW_WIDTH = 4
WINDOW_SLIDES_BY = 1


def load_transcript_file(path, file_format="fasta"):
	"""
	Get a Biopython sequence dict of the whole transcript
	"""
	with open(path) as handle:
		return SeqIO.to_dict(SeqIO.parse(handle, file_format))

def process_single_transcript(transcript_name, transcript_string):
	"""
	Create one document from a transcript name
	"""
	sliding_window_chunks = [transcript_string[i:i+SLIDING_WINDOW_WIDTH] for i in range(0, len(transcript_string)-2, WINDOW_SLIDES_BY)]
	with open(f"{output_dir}/{transcript_name}.txt", "w") as fh:
		fh.write(" ".join(sliding_window_chunks))


def create_all_documents(transcrpt_file, output_dir):
	"""
	Create all documents
	"""
	sequence_dict = load_transcript_file(transcrpt_file)
	for sequence in sequence_dict.keys():
		process_single_transcript(sequence, sequence_dict[sequence])



if __name__ == '__main__':
	if not ( 2 <= len(sys.argv) <= 3):
		print("Usage: python3 protein_chunk_word_generation.py <path to transcript file> [<output_dir>]")
		exit(1)

	output_dir = "." if len(sys.argv == 2) else sys.argv[2]
	if not os.path.isdir(output_dir):
		os.makedirs(output_dir)
	species = sys.argv[1]
	create_all_documents(species, output_dir)