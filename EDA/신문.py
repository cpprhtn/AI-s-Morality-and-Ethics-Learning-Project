#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 18:17:47 2020

@author: cpprhtn
"""



frames = []
df_list = []
import json
import pandas as pd
def read_json(a):
    if a < 1:
        b = 'Error.json'
    elif a < 10:
        b = 'NIRW190000000{}.json'.format(a)
    elif a < 100:      
        b = 'NIRW19000000{}.json'.format(a)
    else:
        b = 'Error.json'
    data = json.load(open(b))
    data2 = data["document"]
    result = []
    for d in data2:
        result.extend(d['paragraph'])
    globals()['df{}'.format(a)]  = pd.DataFrame(result)
    

for i in range(1,31):
    try:
        read_json(i)
        df_list.append(i)
    except FileNotFoundError:
        print("i =", i,"\n 파일이 존재하지 않으므로 건너뜁니다.")
        

for k in df_list: 
    frames.append(globals()['df{}'.format(k)])
    
df0 = pd.concat(frames)

 df0.to_csv("news_paper_1.csv")
 
 
 
 
 
frames = []
df_list = []
import json
import pandas as pd
def read_json(a):
    if a < 1:
        b = 'Error.json'
    elif a < 10:
        b = 'NLRW190000000{}.json'.format(a)
    elif a < 100:      
        b = 'NLRW19000000{}.json'.format(a)
    elif a < 1000:      
        b = 'NLRW1900000{}.json'.format(a)
    else:
        b = 'Error.json'
    data = json.load(open(b))
    data2 = data["document"]
    result = []
    for d in data2:
        result.extend(d['paragraph'])
    globals()['df{}'.format(a)]  = pd.DataFrame(result)
    

for i in range(1,31):
    try:
        read_json(i)
        df_list.append(i)
    except FileNotFoundError:
        print("i =", i,"\n 파일이 존재하지 않으므로 건너뜁니다.")
        

for k in df_list: 
    frames.append(globals()['df{}'.format(k)])
    
df0 = pd.concat(frames)

 df0.to_csv("news_paper_2.csv")




frames = []
df_list = []
import json
import pandas as pd
def read_json(a):
    if a < 1:
        b = 'Error.json'
    elif a < 10:
        b = 'NPRW190000000{}.json'.format(a)
    elif a < 100:      
        b = 'NPRW19000000{}.json'.format(a)
    elif a < 1000:      
        b = 'NPRW1900000{}.json'.format(a)
    else:
        b = 'Error.json'
    data = json.load(open(b))
    data2 = data["document"]
    result = []
    for d in data2:
        result.extend(d['paragraph'])
    globals()['df{}'.format(a)]  = pd.DataFrame(result)
    

for i in range(1,71):
    try:
        read_json(i)
        df_list.append(i)
    except FileNotFoundError:
        print("i =", i,"\n 파일이 존재하지 않으므로 건너뜁니다.")
        

for k in df_list: 
    frames.append(globals()['df{}'.format(k)])
    
df0 = pd.concat(frames)

 df0.to_csv("news_paper_3.csv")
 
 
 
 
frames = []
df_list = []
import json
import pandas as pd
def read_json(a):
    if a < 1:
        b = 'Error.json'
    elif a < 10:
        b = 'NWRW190000000{}.json'.format(a)
    elif a < 100:      
        b = 'NWRW19000000{}.json'.format(a)
    else:
        b = 'Error.json'
    data = json.load(open(b))
    data2 = data["document"]
    result = []
    for d in data2:
        result.extend(d['paragraph'])
    globals()['df{}'.format(a)]  = pd.DataFrame(result)
    

for i in range(1,61):
    try:
        read_json(i)
        df_list.append(i)
    except FileNotFoundError:
        print("i =", i,"\n 파일이 존재하지 않으므로 건너뜁니다.")
        

for k in df_list: 
    frames.append(globals()['df{}'.format(k)])
    
df0 = pd.concat(frames)

 df0.to_csv("news_paper_4.csv")
