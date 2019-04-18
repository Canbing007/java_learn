# -*- coding: utf-8 -*-
# author: Bing
# email: wulitouhaha@vip.qq.com

import numpy as np
import urllib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression

badCase = [
	"""<script></script>""",
	""""><img src=# onerror=alert(/1/)>""",
	"""<script>alert(11)</script>""",
]

goodCase = [
	"""?te=2oildfml&test=sdfhk""",
	""""te=292hsd%2342&test=sdf23hi9ehk==""",
	"""te=2372987893&test=好的首肯定会""",
]

# 数据预处理
def getQueryFromFile(data):
	queries = set()
	for d in data:
		d = d.strip()
		queries.add(d)
	return list(queries)



badQueries = getQueryFromFile( badCase )
tempvalidQueries = getQueryFromFile( goodCase )
tempAllQueries = badQueries + tempvalidQueries

ybad = np.ones(len(badQueries))
ygood = np.zeros(len(tempvalidQueries))
y = np.hstack((ybad, ygood))

print(ybad, ygood, y)

# queries = tempAllQueries
# # 构造3-gram特征，使用TF-IDF提取URL文本特征，并进行文本向量化
# # tokenizer function, this will make 3 grams of each query
# # 构造3-gram特征
# def getNGrams(query):
# 	tempQuery = str(query)
# 	ngrams = []
# 	for i in range(0,len(tempQuery)-3):
# 		ngrams.append(tempQuery[i:i+3])
# 	return ngrams

# # converting data to vectors
# vectorizer = TfidfVectorizer(tokenizer=getNGrams)
# # TF-IDF
# X = vectorizer.fit_transform(queries)
# # splitting data
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# lgs = LogisticRegression()
# # training our model
# lgs.fit(X_train, y_train)
# # checking the accuracy
# print( lgs.score(X_test, y_test) )


# X_predict = [
# 	'AND 1=1',
# 	'ORDER BY 1-- ',
# 	'<script>alert(xss)</script>/',
# 	'and (select substring(@@version,1,1))=\'X\'',
# 	'www.baidu.com',
# 	'<?php @eval($_POST[\'c\']);?>'
# ]

# X_vecpredict = vectorizer.transform(X_predict)
# y_Predict = lgs.predict(X_vecpredict)
 
# #printing predicted values
# mapvalues={1:'Bad ',0:'Good'}
# for i in range(len(X_predict)):
# 	print( mapvalues[y_Predict[i]]+':'+X_predict[i] )
