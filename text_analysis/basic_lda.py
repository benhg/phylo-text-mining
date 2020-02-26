from glob import glob
import os
import sys

from nltk.tokenize import RegexpTokenizer
from gensim.models import Phrases
from nltk.stem.wordnet import WordNetLemmatizer
from gensim.corpora import Dictionary
from gensim.models.ldamulticore import LdaMulticore

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

def lemmatize_docs(docs):
    lemmatizer = WordNetLemmatizer()
    docs = [[lemmatizer.lemmatize(token) for token in doc] for doc in docs]
    return docs

def add_ngrams(docs):
    # Add bigrams and trigrams to docs (only ones that appear 20 times or more).
    bigram = Phrases(docs, min_count=20)
    for idx in range(len(docs)):
        for token in bigram[docs[idx]]:
            if '_' in token:
                # Token is a bigram, add to document.
                docs[idx].append(token)
    return docs

def create_bow(docs):
    # Create a dictionary representation of the documents.
    dictionary = Dictionary(docs)

    # Filter out words that occur less than 20 documents, or more than 50% of the documents.
    dictionary.filter_extremes(no_below=20, no_above=0.5)
    # Bag-of-words representation of the documents.
    corpus = [dictionary.doc2bow(doc) for doc in docs]
    return corpus, dictionary

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
    tokenized_docs = tokenize_docs(documents)
    # lemmatized = lemmatize_docs(tokenized_docs) (don't do this because it;s not english)
    n_grams = add_ngrams(tokenized_docs)
    corpus, dictionary = create_bow(n_grams)

    # Set training parameters.
    num_topics = 10
    chunksize = 2000
    passes = 20
    iterations = 400
    eval_every = None  # Don't evaluate model perplexity, takes too much time.

    # Make a index to word dictionary.
    temp = dictionary[0]  # This is only to "load" the dictionary.
    id2word = dictionary.id2token

    model = LdaMulticore(
        corpus=corpus,
        id2word=id2word,
        num_topics=num_topics,
        )

    top_topics = model.top_topics(corpus) #, num_words=20)

    # Average topic coherence is the sum of topic coherences of all topics, divided by the number of topics.
    avg_topic_coherence = sum([t[1] for t in top_topics]) / num_topics
    print('Average topic coherence: %.4f.' % avg_topic_coherence)

    from pprint import pprint
    pprint(top_topics)

    import pyLDAvis.gensim
    import pyLDAvis
    #  pyLDAvis.enable_notebook()
    vis = pyLDAvis.gensim.prepare(model, corpus, dictionary=dictionary)
    pyLDAvis.save_html(vis, open("lda_vis.html", "w"))





