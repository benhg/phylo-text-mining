# phylo-text-mining
Applying text-mining techniques to phylogenetic analysis

## Abstract

This project applies the Latent Dirichlet Allocation (LDA) and to the task of molecular phylogenetic analysis.  An important property of the LDA is that it analyzes only the distribution of words in documents relative to the language as a whole. The only assumptions it depends on are the existence of “words,” which they treat as the smallest unit of linguistic meaning, and “documents” which are simply collections of words that make up one unit the user wishes to analyze. The topic-models that these algorithms generate can be incredibly useful. To create one, a set of documents is fed into the model, each being made up of words. The LDA then analyzes the relationship of the words inputted, both within each document, and within the whole set of documents to be analyzed. Using information about word frequency, document frequency, word and document size, and commonality of words, the LDA is able to generate groups of words which it has inferred are closely related to each other. These groups of words can be interpreted as topics. The LDA also gives a measure of how closely related each topic is to each other topic. In this version of the LDA process, we create a set of documents which represent a single species, and extract “topics,” which we consider to be semantically informative of the species’s genome. We then use these semantic units to search for similarity and relationships.

## Background Info

An idea that I have been interested in for quite some time involves applying a mathematical analysis technique developed for text mining, applied to the context of phylogenetic analysis. This text-mining approach is called the Latent Dirichlet Allocation (LDA), and it’s designed to extract important groups of words out of documents, with the goal of defining a document as a group of related sets of words, each of which represent a topic. A related algorithm, the Hierarchical Latent Dirichlet Allocation (HLDA) is designed to not only find important topics but also to infer hierarchical relationships between said topics. In both of these contexts, a “topic” can be thought of as a “group of words.” An important property of the LDA and HLDA is that they are not language-specific, rather analyzing only the distribution of words in documents and in the language as a whole. The only assumptions they depend on are the existence of “words,” which they treat as the smallest unit of linguistic meaning, and “documents” which are simply collections of words that make up one unit the user wishes to analyze.


The topic-models that these algorithms generate can be incredibly useful. To create one, you feed into the model a set of documents, each made up of words. The LDA then analyzes the relationship of the words inputted, both within each document, and within the whole set of documents to be analyzed. Using information about word frequency, document frequency, word and document size, and commonality of words, the LDA is able to generate groups of words which it has inferred are closely related to each other. These groups of words can be interpreted as topics. For example, if I plugged several sports-related newspaper articles into the LDA, it might tell me that one topic was made up of “basket, hoop, center, screen, jump,” while it would tell me that another topic was made up of the words “base, glove, pitch, run, strike”. I could then use a separate algorithm to label these topics with “basketball” and “baseball,” respectively. The LDA also gives a measure of how closely related each topic is to each other topic. The HLDA might be able to do one step better - in addition to what the LDA does, it might say that my “basketball” and “baseball” topics were both contained by a topic, made up of “team, ball, fan, win, television”.


The main idea of this project is to take this exact technique and instead of applying it to language, apply it to the genomes of various species, to infer relationships between genes. With the normal text-based LDA, our two simplifying assumptions are that each document is made up of a mixture of topics and each topic is made up of a mixture of words. In this version of the LDA, I would create “documents,” each representing one genome, which would be made up of “words,” each of which would be a subset of a gene (or pseudogene, or intron). Then, I would feed the “documents” into the LDA, to see what “topics” it comes up with. These “topics” should roughly represent a gene, and the topic relationships should tell us how these approximations for genes are related to each other. We can then reconstruct the relationship between genomes from this information. Additionally, the HLDA of the same input data should provide us with information about an approximation of the gene tree.


## Submodules

I've divided up this repo into the following submodules, for ease of maintainability:

1. raw_data:
	
	The raw data section is where i'm going to be keeping two sets of raw data from GenBank - for now, the two families i'm working in are primates, where I plan to use Cytochrome Oxidase subunits A, B, and C, and some yet undetermined viruses, wehere I will use whole genomes.

2. data_processing:

	This is where I keep scripts that will help me turn the raw data into data that is usable in an LDA/HLDA - words and documents. There will be several subunits here, in each of which i'll keep the processed data and the script that processed it.

3. text_analysis

	This is where the actual text analysis code will be kept and output therefrom will be found.






