import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
nltk.download('wordnet')
from nltk.corpus import stopwords

import pandas as pd
import numpy as np


#1
def basic_clean(string):
    string = string.lower()
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    string = re.sub(r"[^a-z0-9'\s]", '', string)
    return string
#2
def tokenize_string(string):
    tokenizer = nltk.tokenize.ToktokTokenizer()
    string = tokenizer.tokenize(string, return_str=True)
    return string

#3
def stem_string(string):
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in string.split()]
    string_stemmed = ' '.join(stems)
    return string_stemmed

#4
def lemmatize_string(string):
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    string_lemmatized = ' '.join(lemmas)
    return string_lemmatized

#5
def adjust_stopwords(string, addlist = [], removelist = []):
    stopword_list = stopwords.words('english')
    
    for word in removelist:
        stopword_list.remove(word)
     
    for word in addlist:
            stopword_list.append(word)
            
    words = string.split()
    filtered_words = [w for w in words if w not in stopword_list]
    print('Removed {} stopwords'.format(len(words) - len(filtered_words)))
    print('---')
    
    article_without_stopwords = ' '.join(filtered_words)
    
    return article_without_stopwords
    
    
    
    
    
    


    
    




    
    

