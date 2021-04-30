"""
Topic Modeling with gensim and pyLDAvis
Created by Sophia Horner for ACM Research, Interpreting Historical Data Using Text Mining Extraction
https://github.com/ACM-Research/text-mining-extraction
"""

# Requires pyLDAvis 3.2.2
import gensim.corpora.dictionary
import pyLDAvis.gensim
from tqdm import tqdm
import numpy as np
import pandas as pd
import nltk
import requests, csv, urllib.request
import os
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('stopwords')

from nltk.corpus import stopwords
stop=set(stopwords.words('english'))

toc = pd.read_csv("Annotations Spreadsheet.csv")

# Different corpus for each demographic
econ_status = {"P":[], "M":[], "U":[]}
race_status = {"B":[], "W":[]}
gender_status = {"F":[], "M":[]}
rel_status = {"Y":[], "N":[]}
mil_status = {"Y":[], "N":[]}
statuses = {"Economic Status: ":econ_status, "Race: ":race_status, "Gender: ":gender_status, "Religious/Spiritual Content: ":rel_status,  "Military Status: ":mil_status}
other_corpus = []
lda_models = [None] * 16

# Interaction
topics = 4
mode = 1
outputName = "Default"
customUrl = ""

print("Choose a mode: ")
print("0 - Single file analysis with custom URL")
print("1 - Total collection analysis")
print("2 - Analysis by demographic")
mode = int(input())

print("Enter number of topics: ")
topics = int(input())

print("Enter identifying name for output file: ")
outputName = input()

if mode == 0:
    print("Enter custom URL: ")
    customUrl = input()

# Removes stopwords and lemmatizes
def cleanText(target):
    print(target)
    response = urllib.request.urlopen(target)
    f_text = [l.decode('utf-8') for l in response.readlines()]

    lem=WordNetLemmatizer()
    for l in tqdm(f_text):
        words=[w.lower() for w in word_tokenize(l) if (w.lower() not in stop)]
        words=[lem.lemmatize(w) for w in words if (len(w)>2 and (w not in stop))]
        yield words

# Creates LDAmodel from corpus and saves visualization
def createLDA(corpus, topics, outputName):
    dic=gensim.corpora.Dictionary(corpus)
    bow_corpus=[dic.doc2bow(doc) for doc in corpus]

    lda_model = gensim.models.LdaModel(tqdm(bow_corpus),
                                    num_topics=topics,
                                    id2word = dic,
                                    passes = 10)

    vis = pyLDAvis.gensim.prepare(lda_model, bow_corpus, dic)
    pyLDAvis.save_html(vis, "output{}.html".format(outputName))


if mode == 0:
    # Single text mode
    for i in cleanText(customUrl):
        other_corpus.append(i)
else:
    for i, x in enumerate(toc['URL(text-only)']):
        for words in cleanText(x):
            # Total corpus mode
            if mode == 1:
                other_corpus.append(words)
            # Demographic mode
            elif mode == 2:
                for category in statuses:
                    for status in statuses[category]:
                        if category + status in toc["Demographic Data"][i]:
                            statuses[category][status].append(words)

if mode == 2:
    for i, category in enumerate(statuses):
        for j, status in enumerate(statuses[category]):
            demOutputName = outputName + category + status
            createLDA(statuses[category][status], topics, demOutputName)
else:
    createLDA(other_corpus, topics, outputName)

"""
    # Analysis of topic distances
    doc_domestic = ['church', 'family', 'school']
    doc_slavery = ['plantation', 'slavery', 'freedom']
    doc_war = ['army', 'battle', 'general']

    for i, model in enumerate(lda_models):
        if model is not None:
            bow_domestic = model.id2word.doc2bow(doc_domestic)
            bow_slavery = model.id2word.doc2bow(doc_slavery)
            bow_war = model.id2word.doc2bow(doc_war)

            lda_bow_domestic = model[bow_domestic]
            lda_bow_slavery = model[bow_slavery]
            lda_bow_war = model[bow_war]

            print("\nNumber " + str(i) + ": ")
            from gensim.matutils import hellinger
            print("Domestic vs Slavery")
            print(hellinger(lda_bow_domestic, lda_bow_slavery))
            print("Slavery vs War")
            print(hellinger(lda_bow_slavery, lda_bow_war))
            print("War vs Domestic")
            print(hellinger(lda_bow_war, lda_bow_domestic))
"""