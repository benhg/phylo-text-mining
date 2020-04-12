import sys

"""
Uniform Chunking approach. In this methodology,
we chunk each gene sequence into uniform-length "words"

For now, we're using "text-document like" files, which means
that we're putting everything into plain text files with
space-separated chunks
"""

# define uniform chunk size
CHUNK_SIZE = 7


def chunk_uniform(input_gene, chunk_size=CHUNK_SIZE):
    return [input_gene[i:i + chunk_size]
            for i in range(0, len(input_gene), chunk_size)]


def read_from_file(species):
    pass


def create_chunked_file(species, output_dir="."):
    unchunked_data = read_from_file(species)
    chunked_data = chunk_uniform(unchunked_data)
    with open(f"{output_dir}/{species}.txt") as fh:
        for chunk in chunked_data:
            fh.write(f"{chunk} ")


if __name__ == '__main__':
    if not (2 < len(sys.argv) < 3):
        print("Usage: python3 uniform_chunking.py <species> [<output_dir>]")
        exit(1)

    output_dir = "." if len(sys.argv == 2) else sys.argv[2]
    species = sys.argv[1]
    create_chunked_file(species, output_dir)
