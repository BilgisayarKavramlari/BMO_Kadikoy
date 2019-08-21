#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:22:28 2019

@author: sadievrenseker
"""

import pandas as pd
veri = pd.read_excel('kadikoy_cinsiyet.xlsx')
veri = veri.iloc[:,:2]

from sklearn.cluster import KMeans
km = KMeans(n_clusters = 5)
sonuc = km.fit_predict(veri)
print(sonuc)

from sklearn.cluster import AgglomerativeClustering 
ac = AgglomerativeClustering(n_clusters = 5)
sonuc2 = ac.fit_predict(veri)
print(sonuc2)

from sklearn.preprocessing import MinMaxScaler
mms = MinMaxScaler()
normal = mms.fit_transform(veri)

from sklearn.cluster import DBSCAN
dbs = DBSCAN(eps=0.2, min_samples=3)
sonuc3 = dbs.fit_predict(normal)
print(sonuc3)