#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:01:08 2019

@author: sadievrenseker
"""

import pandas as pd
veri = pd.read_excel('emlak_fiyat.xlsx')
print(veri)

semt = veri.iloc[:,1:2].values
print(semt)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
semt[:,0] = le.fit_transform(semt[:,0])
print(semt)

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features='all')
semt=ohe.fit_transform(semt).toarray()
print(semt)

balkon = veri.iloc[:,5]
otopark = veri.iloc[:,4]
balkon = le.fit_transform(balkon)
otopark = le.fit_transform(otopark)
print(balkon)
print(otopark)

sayisal_kolonlar = veri[['m2','oda','kat','fiyat']]


semt_df = pd.DataFrame(data = semt, index = range(10), columns=['kadikoy','umraniye','uskudar'] )
balkon_df = pd.DataFrame(data = balkon , index = range(10), columns=['balkon'])
otopark_df = pd.DataFrame(data = otopark , index = range(10), columns=['otopark'])

sonuc = pd.concat([semt_df,balkon_df,otopark_df,sayisal_kolonlar],axis=1)

print(sonuc)

x = sonuc.iloc[:,:8]
y = sonuc.iloc[:,8:]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(X_train,y_train)
tahmin = lr.predict(X_test)
print(tahmin)
print(y_test)


from sklearn.svm import SVR
svr = SVR(kernel='poly')

svr.fit(X_train,y_train)
tahmin = svr.predict(X_test)
print(tahmin)
print(y_test)


from sklearn.ensemble import RandomForestRegressor
rfr = RandomForestRegressor()
rfr.fit(X_train,y_train)
tahmin = rfr.predict(X_test)
print(tahmin)
print(y_test)






