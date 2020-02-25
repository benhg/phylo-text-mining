# Data Processing

This is where I will keep the processing scripts, and the LDA-ready processed data.

I will use several methods of mungifying data to get it ready for use in the LDA model. That mungifying will require that we are able to enforce the following two assumptions in our data -

- That we can break down each species into a "document"
- That each "document" is made up of "semantic units" - ie words.

After this, we can try to run an LDA or HLDA on the transformed data. Each methodology will have its own subdirectory in this directory, and they will each have some description about why I've done what I've done.

## Subunits

There are subunits for "stemming," and for the various data-processing methodologies 

## Current List of Methodologies

The following is a list of the methodologies / scripts included in this module

1. Whole-Gene
	
	With this method, we treat each gene in the dataset as a "word". This results in long words.

2. Uniform chunk
	
	In this method, we create chunks of uniform length of each genome, and add them into documents

3. Random Chunk
	
	In this method, we create chunks of random length from each species, creating documents from them

4. Sequence based

	In this method, we use sequences as words, with lengths on the order of hundreds of base-pairs.

	We can also create arbitrarily shorter ones, by creating chunks based on pieces of each sequence.

5. Protein-based version

	After consulting with a real biologist, I found that creating words based on a "sliding window" of amino acid sequences of a fixed length (four was suggested) in documents.