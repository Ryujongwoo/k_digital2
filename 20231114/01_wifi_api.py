#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings(action='ignore')


# In[2]:


import requests
import json
import xmltodict # xml 데이터를 딕셔너리로 변환하기 위해 import 한다.


# In[17]:


# 서울시 공공 와이파이 정보를 요청한다.
# http://openapi.seoul.go.kr:8088/인증키/xml/TbPublicWifiInfo/시작/끝/
apiRequest = 'http://openapi.seoul.go.kr:8088/746e4968796d6b7639366763624a53/xml/TbPublicWifiInfo/1/1/'
response = requests.get(apiRequest)
# print(response)
# print(type(response.text))
print(response.text) # xml
print('=' * 80)

# 응답받은 xml 형태의 문자열 데이터를 딕셔너리로 변환한다.
dictionary = xmltodict.parse(response.text)
# print(type(dictionary)) # dict
print(dictionary)
print('=' * 80)

# xml 형태를 변환한 딕셔너리 데이터를 json 데이터로 변환한다.
# dumps() 메소드는 인수로 지정된 딕셔너리를 json 타입을 변환한다.
# ensure_ascii옵션을 False 지정해서 한글 깨짐을 방지한다.
# indent 옵션을 지정하면 json 타입으로 변경된 데이터가 보기좋게 만들어진다.
json_object = json.dumps(dictionary, ensure_ascii=False, indent=2)
print(type(json_object))
print(json_object)


# In[ ]:




