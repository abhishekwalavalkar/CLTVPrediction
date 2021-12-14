#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import json
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

url = 'https://cltv-prediction.herokuapp.com/predict_api'

headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
data_dict={'Customer ID': 100108491}
r = requests.post(url, json=data_dict)
print(r, r.text)

