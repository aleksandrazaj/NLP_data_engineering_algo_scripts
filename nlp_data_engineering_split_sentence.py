#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import requests
import pandas as pd
from pandas.io.json import json_normalize
import json

import pyodbc
from sqlalchemy import create_engine
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
import datetime
import time
from datetime import timedelta
import struct
import logging

#Azure SQL data
server = 'blank'
database = 'blank'
username = 'blank'
password = 'blank'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#Read Finc3 DataTable from SQL
df = pd.read_sql_query(
        '''blank''', cnxn)

# Specify the triger for what Azure will listen and terminate container
def termination_trigger():
    print('execution stopped')

def setup_tokenizer():
    punkt_param = PunktParameters()
    abbrevations = ['u.s.a.', 'app','etc','i.e','h.p','cfg','imp','b.b','ssf','d.c','u.s','eq','vs','1','2','3','4','5','6','7','8','9']
    punkt_param.abbrev_types = set(abbrevations)
    tokenizer = PunktSentenceTokenizer(punkt_param)
    return tokenizer

def splitting_uf_to_sent(df):
    df_sentences=pd.DataFrame(columns=['review_id','lineNo', 'sentence'])
    for index,row in df.iterrows():
        lineNo = 0
        review_id=row[0]
        text=row[1]
        sentences = tokenizer.tokenize(text)
        for sentence in sentences:
            df_sentences=df_sentences.append({'review_id':str(review_id), 'lineNo':lineNo, 'sentence':str(sentence)}, ignore_index=True)
            lineNo = lineNo +1
    return df_sentences

tokenizer=setup_tokenizer()
df_sentences=splitting_uf_to_sent(df)
#saveReviewSentence(df_sentences)

cursor.close()
cnxn.close()

termination_trigger()


# In[ ]:


df_sentences = df_sentences.drop_duplicates(subset = ['review_id','lineNo'], keep = 'last')
df_sentences.info()
df_sentences.head(100)


# In[ ]:




