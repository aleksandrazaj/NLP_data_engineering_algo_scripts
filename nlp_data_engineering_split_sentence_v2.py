#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
df = pd.read_excel('_.xlsx')
df.info()


# In[ ]:


df.head()


# In[ ]:


id_index = df[['Link','sentence']].set_index('Link')
new = id_index['sentence'].str.replace('\n', '', regex=False)


# In[ ]:


#id_index = df[['id','text']].set_index('id')
split = new.str.split('.').apply(pd.Series,1).stack()
df_new = split.to_frame()
df_new1 = df_new.reset_index(level=[0,1])
df_new2 = df_new1.dropna()
df_new2 = df_new2.rename(columns={"level_1": "lineNo"})


# In[ ]:


rest_of_Data = df[['Media','Link','Country','Month/year','Rating','Award']]
result = pd.merge(rest_of_Data, df_new2, on=['Link'])
result


# In[ ]:


import numpy as np
dff = result.replace(r'^\s*$', np.nan, regex=True)
dff1 = dff[dff[0].notna()]
dff2 = dff1.rename(columns={0: "text"})

