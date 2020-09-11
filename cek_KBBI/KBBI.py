import json as js
from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path +'/dataKBBI.json', 'r') as outfile:
    corpus_ = js.load( outfile)
# print(corpus)

def cek_kbbi(kalimat, corpus=[], corpus_=corpus_):
    corpus_ = corpus_+corpus
    kalimat = tknzr.tokenize(kalimat.lower())
    new_kalimat = ""
    for i in kalimat:
        if i in corpus_:
            i = i+" "
            new_kalimat += i
    return new_kalimat.rstrip()
