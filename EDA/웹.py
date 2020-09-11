#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 20:42:48 2020

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
        b = 'EBRW190300000{}.json'.format(a)
    elif a < 100:      
        b = 'EBRW19030000{}.json'.format(a)
    elif a < 1000:      
        b = 'EBRW1903000{}.json'.format(a)
    elif a < 10000:      
        b = 'EBRW190300{}.json'.format(a)
    else:
        b = 'Error.json'
    data = json.load(open(b))
    data2 = data["document"]
    result = []
    for d in data2:
        result.extend(d['paragraph'])
    globals()['df{}'.format(a)]  = pd.DataFrame(result)
    

for i in range(2753,2764):
    try:
        read_json(i)
        df_list.append(i)
    except FileNotFoundError:
        print("i =", i,"\n 파일이 존재하지 않으므로 건너뜁니다.")
        

for k in df_list: 
    frames.append(globals()['df{}'.format(k)])
    
df0 = pd.concat(frames)

 df0.to_csv("web_1.csv")
 
 
 
 
frames = []
df_list = []
import json
import pandas as pd
def read_json(a):
    if a < 1:
        b = 'Error.json'
    elif a < 10:
        b = 'EBRW190800000{}.json'.format(a)
    elif a < 100:      
        b = 'EBRW19080000{}.json'.format(a)
    elif a < 1000:      
        b = 'EBRW1908000{}.json'.format(a)
    else:
        b = 'Error.json'
    data = json.load(open(b))
    data2 = data["document"]
    result = []
    for d in data2:
        result.extend(d['paragraph'])
    globals()['df{}'.format(a)]  = pd.DataFrame(result)
    

for i in range(1,308):
    try:
        read_json(i)
        df_list.append(i)
    except FileNotFoundError:
        print("i =", i,"\n 파일이 존재하지 않으므로 건너뜁니다.")
        

for k in df_list: 
    frames.append(globals()['df{}'.format(k)])
    
df0 = pd.concat(frames)

df0.to_csv("web_2.csv")
 
 
 
 
 
frames = []
df_list = []
import json
import pandas as pd
def read_json(a):
    if a < 1:
        b = 'Error.json'
    elif a < 10:
        b = 'EBRW190810000{}.json'.format(a)
    elif a < 100:      
        b = 'EBRW19081000{}.json'.format(a)
    elif a < 1000:      
        b = 'EBRW1908100{}.json'.format(a)
    else:
        b = 'Error.json'
    data = json.load(open(b))
    data2 = data["document"]
    result = []
    for d in data2:
        result.extend(d['paragraph'])
    globals()['df{}'.format(a)]  = pd.DataFrame(result)
    

for i in range(1,272):
    try:
        read_json(i)
        df_list.append(i)
    except FileNotFoundError:
        print("i =", i,"\n 파일이 존재하지 않으므로 건너뜁니다.")
        

for k in df_list: 
    frames.append(globals()['df{}'.format(k)])
    
df0 = pd.concat(frames)

df0.to_csv("web_3.csv")





frames = []
df_list = []
import json
import pandas as pd
def read_json(a):
    if a < 1:
        b = 'Error.json'
    elif a < 10:
        b = 'ERRW190500000{}.json'.format(a)
    elif a < 100:      
        b = 'ERRW19050000{}.json'.format(a)
    elif a < 1000:      
        b = 'ERRW1905000{}.json'.format(a)
    elif a < 10000:      
        b = 'ERRW190500{}.json'.format(a)
    else:
        b = 'Error.json'
    data = json.load(open(b))
    data2 = data["document"]
    result = []
    for d in data2:
        result.extend(d['paragraph'])
    globals()['df{}'.format(a)]  = pd.DataFrame(result)
    

for i in range(308,2780):
    try:
        read_json(i)
        df_list.append(i)
    except FileNotFoundError:
        print("i =", i,"\n 파일이 존재하지 않으므로 건너뜁니다.")
        

for k in df_list: 
    frames.append(globals()['df{}'.format(k)])
    
df0 = pd.concat(frames)

df0.to_csv("web_4.csv")





frames = []
df_list = []
import json
import pandas as pd
def read_json(a):
    if a < 1:
        b = 'Error.json'
    elif a < 10:
        b = 'ESRW190500000{}.json'.format(a)
    elif a < 100:      
        b = 'ESRW19050000{}.json'.format(a)
    elif a < 1000:      
        b = 'ESRW1905000{}.json'.format(a)
    elif a < 10000:      
        b = 'ESRW190500{}.json'.format(a)
    else:
        b = 'Error.json'
    data = json.load(open(b))
    data2 = data["document"]
    result = []
    for d in data2:
        result.extend(d['paragraph'])
    globals()['df{}'.format(a)]  = pd.DataFrame(result)
    

for i in range(307,2782):
    try:
        read_json(i)
        df_list.append(i)
    except FileNotFoundError:
        print("i =", i,"\n 파일이 존재하지 않으므로 건너뜁니다.")
        

for k in df_list: 
    frames.append(globals()['df{}'.format(k)])
    
df0 = pd.concat(frames)

df0.to_csv("web_5.csv")





frames = []
df_list = []
import json
import pandas as pd
def read_json(a):
    if a < 1:
        b = 'Error.json'
    elif a < 10:
        b = 'ESRW190510000{}.json'.format(a)
    elif a < 100:      
        b = 'ESRW19051000{}.json'.format(a)
    elif a < 1000:      
        b = 'ESRW1905100{}.json'.format(a)
    elif a < 10000:      
        b = 'ESRW190510{}.json'.format(a)
    else:
        b = 'Error.json'
    data = json.load(open(b))
    data2 = data["document"]
    result = []
    for d in data2:
        result.extend(d['paragraph'])
    globals()['df{}'.format(a)]  = pd.DataFrame(result)
    

for i in range(308,1171):
    try:
        read_json(i)
        df_list.append(i)
    except FileNotFoundError:
        print("i =", i,"\n 파일이 존재하지 않으므로 건너뜁니다.")
        

for k in df_list: 
    frames.append(globals()['df{}'.format(k)])
    
df0 = pd.concat(frames)

df0.to_csv("web_6.csv")
