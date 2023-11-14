#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings(action='ignore')



# In[2]:


# pip install elasticsearch
from elasticsearch import Elasticsearch # 파이썬에서 elasticsearch와 연동하기 이해 import 한다.


# In[3]:


# elasticsearch 객체를 만든다.
es = Elasticsearch('http://localhost:9200/')


# In[4]:


# elasticsearch에 인덱싱할 도큐먼트를 딕셔너리 형태로 만든다.
doc = {'name': 'kim', 'age': 25}
print(doc)

# elasticsearch 객체의 index() 메소드로 엘라스틱서치에 인덱싱한다.
# index(index='인덱스이름', id=아이디, body=도큐먼트)
response = es.index(index='python_index', id=1, body=doc)
print(response)
print('=' * 80)


# In[5]:


# elasticsearch 객체의 search() 메소드에서 실행할 쿼리를 딕셔너리 형태로 만든다.
query = {
    "size": 1,
    "query": {
        "match": {
            "name": "kim"
        }
    }
}

# search(index='인덱스이름', body=쿼리) 
response = es.search(index='python_index', body=query)
print(response)
print('=' * 80)


# In[6]:


query = {
    "size": 1,
    "query": {
        "term": {
            "name.keyword": "kim"
        }
    }
}
response = es.search(index='python_index', body=query)
print(response)
print('=' * 80)


# In[7]:


query = {
    "size": 1,
    "query": {
        "term": {
            "DestCityName": {
                "value": "Seoul"
            }
        }
    }
}
response = es.search(index='kibana_sample_data_flights', body=query)
print(response)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




