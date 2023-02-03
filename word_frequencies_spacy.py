#!/usr/bin/env python
# coding: utf-8

# In[104]:


import sklearn
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation


# In[ ]:


import pandas as pd
data = pd.read_excel('file.xlsx')
data = data[['sentence']]
data = data.to_string()


# In[107]:


stopwords = list(STOP_WORDS)


# In[108]:


nlp = spacy.load('en_core_web_sm')
nlp.max_length = 5600000


# In[109]:


doc = nlp(data)


# In[110]:


tokens = [token.text for token in doc]
print(tokens)


# In[111]:


punctuation = punctuation + '\n' + '..' + '\d+' + '                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ' + '0' + '1' + '2' + '3' + '4' + '5' + ' 6' + '7' + '8' + '9'
punctuation


# In[112]:


word_frequencies = {}
for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1
                
print(word_frequencies)


# In[113]:


max_frequency = max(word_frequencies.values())
max_frequency


# In[114]:


for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word]/max_frequency

print(word_frequencies)


# In[115]:


df = pd.DataFrame.from_dict(word_frequencies, orient='index')

df


# In[116]:


df = df.reset_index()


# In[117]:


df = df.rename(columns = {'index':'word', 0:'frequency_score'})


# In[120]:


df = df.groupby(['frequency_score'], sort=True)
df.head()


# In[ ]:




