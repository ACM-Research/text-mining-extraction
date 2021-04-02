import gensim
import gensim.corpora.dictionary
import pyLDAvis.gensim
from tqdm import tqdm
import pandas as pd
import numpy as np
import nltk
import requests, csv, urllib.request
import os
from nltk.stem import WordNetLemmatizer,PorterStemmer
from nltk.tokenize import word_tokenize
import gensim
from multiprocessing import Process, freeze_support
import pyLDAvis
import pyLDAvis.gensim
from tqdm import tqdm
from gensim.models.coherencemodel import CoherenceModel
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

from nltk.corpus import stopwords

import warnings
warnings.filterwarnings(action="once")

stop=set(stopwords.words('english'))

url = 'https://raw.githubusercontent.com/ACM-Research/text-mining-extraction/main/first-person-narratives-american-south/data/toc.csv'
response = urllib.request.urlopen(url)
toc = pd.read_csv(response)

corpus=[]
for x in toc['URL(text-only)']:

    response = urllib.request.urlopen(x)
    f_text = [l.decode('utf-8') for l in response.readlines()]

    stem=PorterStemmer()
    lem=WordNetLemmatizer()
    for l in tqdm(f_text):
        words=[w.lower() for w in word_tokenize(l) if (w.lower() not in stop)]
        words=[lem.lemmatize(w) for w in words if len(w)>2]
        corpus.append(words)

dic=gensim.corpora.Dictionary(corpus)
bow_corpus=[dic.doc2bow(doc) for doc in corpus]

lda_model = gensim.models.LdaModel(tqdm(bow_corpus),
                                    num_topics=4,
                                    id2word = dic,
                                    passes = 10)

vis = pyLDAvis.gensim.prepare(lda_model, bow_corpus, dic)
pyLDAvis.save_html(vis, "output.html")
