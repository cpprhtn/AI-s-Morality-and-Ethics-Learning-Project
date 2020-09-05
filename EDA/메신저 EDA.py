#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 16:34:14 2020

@author: cpprhtn
"""
a='1'
b = 'MDRW190000000{}.json'.format(a)


import json
import pandas as pd
def read_json(a):
    if a < 1:
        b = 'Error.json'
    elif a < 10:
        b = 'MDRW190000000{}.json'.format(a)
    elif a < 100:      
        b = 'MDRW19000000{}.json'.format(a)
    elif a< 1000:
        b = 'MDRW1900000{}.json'.format(a)
    else:
        b = 'Error.json'
    data = json.load(open(b))
    data2 = data["document"]
    result = []
    for d in data2:
        result.extend(d['utterance'])
    globals()['df{}'.format(a)]  = pd.DataFrame(result)
    

for i in range(1,401):
    try:
        read_json(i)
        
    except FileNotFoundError:
        print("i =", i,"\n 파일이 존재하지 않으므로 건너뜁니다.")
        
