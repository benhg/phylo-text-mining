import sys
import random

"""
Random Chunking approach. In this methodology,
we chunk each gene sequence into random-length "words"

For now, we're using "text-document like" files, which means
that we're putting everything into plain text files with
space-separated chunks
"""

# minimum and maximum chunk sizes
CHUNK_MIN = 1
CHUNK_MAX = 18


def chunk_random(input_gene, chunk_size=CHUNK_SIZE):
    chunks = []
    current = 0
    while True:
        try:
            next_chunk_size = random.randint(CHUNK_MIN, CHUNK_MAX)
            chunks.append(input_gene[current:current + next_chunk_size])
            current += next_chunk_size
        except Exception as e:
            # We've hit the end of the gene
            chunks.append(inp1ut_gene[current:])
            break

    return chunks


def read_from_file(species):
    pass


def create_chunked_file(species, output_dir="."):
    unchunked_data = read_from_file(species)
    chunked_data = chunk_random(unchunked_data)
    with open(f"{output_dir}/{species}.txt") as fh:
        for chunk in chunked_data:
            fh.write(f"{chunk} ")


if __name__ == '__main__':
    if not (2 < len(sys.argv) < 3):
        print("Usage: python3 random_chunking.py <species> [<output_dir>]")
        exit(1)

    output_dir = "." if len(sys.argv == 2) else sys.argv[2]
    species = sys.argv[1]
    create_chunked_file(species, output_dir)
