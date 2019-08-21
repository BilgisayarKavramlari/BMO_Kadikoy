#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:49:51 2019

@author: sadievrenseker
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

veri = pd.read_excel('sepet_bmo.xlsx')

records = []
for i in range(0, 11):
    records.append([str(veri.values[i,j]) for j in range(0, 5)])
    
association_rules = apriori(records, min_support=0.05, min_length=2)
association_results = list(association_rules)

for i in range(len(association_results)):
    print(association_results[i])
#print(association_rules[0])
