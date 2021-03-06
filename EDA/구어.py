#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 20:05:43 2020

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
        b = 'SARW190000000{}.json'.format(a)
    elif a < 100:      
        b = 'SARW19000000{}.json'.format(a)
    elif a< 1000:
        b = 'SARW1900000{}.json'.format(a)
    elif a < 10000:
        b = 'SARW190000{}.json'.format(a)
    elif a < 100000:
        b = 'SARW19000{}.json'.format(a)
    else:
        b = 'Error.json'
    data = json.load(open(b))
    data2 = data["document"]
    result = []
    for d in data2:
        result.extend(d['utterance'])
    globals()['df{}'.format(a)]  = pd.DataFrame(result)
    

for i in range(1,1180):
    try:
        read_json(i)
        df_list.append(i)
    except FileNotFoundError:
        print("i =", i,"\n 파일이 존재하지 않으므로 건너뜁니다.")
        

for k in df_list: 
    frames.append(globals()['df{}'.format(k)])
    
df0 = pd.concat(frames)

del df0['original_form']


 df0.to_csv("spoken_language_1.csv")
 
 
 
frames = []
df_list = []
def read_json(a):
    if a < 1:
        b = 'Error.json'
    elif a < 10:
        b = 'SDRW190000000{}.json'.format(a)
    elif a < 100:      
        b = 'SDRW19000000{}.json'.format(a)
    elif a< 1000:
        b = 'SDRW1900000{}.json'.format(a)
    elif a < 10000:
        b = 'SDRW190000{}.json'.format(a)
    else:
        b = 'Error.json'
    data = json.load(open(b))
    data2 = data["document"]
    result = []
    for d in data2:
        result.extend(d['utterance'])
    globals()['df{}'.format(a)]  = pd.DataFrame(result)
    

for i in range(1,2140):
    try:
        read_json(i)
        df_list.append(i)
    except FileNotFoundError:
        print("i =", i,"\n 파일이 존재하지 않으므로 건너뜁니다.")
        

for k in df_list: 
    frames.append(globals()['df{}'.format(k)])
    
df0 = pd.concat(frames)

del df0['original_form']


 df0.to_csv("spoken_language_2.csv")



frames = []
df_list = []
def read_json(a):
    if a < 1:
        b = 'Error.json'
    elif a < 10:
        b = 'SERW190000000{}.json'.format(a)
    elif a < 100:      
        b = 'SERW19000000{}.json'.format(a)
    elif a< 1000:
        b = 'SERW1900000{}.json'.format(a)
    elif a < 10000:
        b = 'SERW190000{}.json'.format(a)
    elif a < 100000:
        b = 'SERW19000{}.json'.format(a)
    else:
        b = 'Error.json'
    data = json.load(open(b))
    data2 = data["document"]
    result = []
    for d in data2:
        result.extend(d['utterance'])
    globals()['df{}'.format(a)]  = pd.DataFrame(result)
    

for i in range(1001,75070):
    try:
        read_json(i)
        df_list.append(i)
    except FileNotFoundError:
        print("i =", i,"\n 파일이 존재하지 않으므로 건너뜁니다.")
        

for k in df_list: 
    frames.append(globals()['df{}'.format(k)])
    
df0 = pd.concat(frames)

del df0['original_form']


 df0.to_csv("spoken_language_3.csv")
