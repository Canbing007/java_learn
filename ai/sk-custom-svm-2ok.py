# -*- coding: utf-8 -*-
# author: Bing
# email: wulitouhaha@vip.qq.com

import sklearn, re
from sklearn.model_selection import train_test_split
from sklearn import cross_validation
from sklearn import datasets
from sklearn import svm
from sklearn.externals import  joblib
from sklearn.metrics import classification_report
from sklearn.externals import joblib
from sklearn import metrics
from sklearn import preprocessing

x = []
y = []

# 判断特征维度
def get_evil_char(url):
	# 判断符号的出现的个数，做为一个维度
    return len(re.findall("[<>,\'\"/]", url, re.IGNORECASE))

def get_evil_word(url):
	# 判断关键词的出现的个数，做为一个维度
    return len(re.findall("(alert)|(script=)|(eval)|(src=)|(prompt)|(onerror)|(onload)|(onfocus)|(onmouseover)|(string.fromcharcode)|(document.cookie)|(%3c)|(%3e)|(%20)|(iframe)|(href)|(javascript)|(data)",url,re.IGNORECASE))

def get_feature(url):
    return [ get_evil_char(url), get_evil_word(url) ]

def labels(filename,data,label):
    with open(filename, "rb") as f:
        for line in f:
            data.append(get_feature(line.decode().strip()))
            if label:
                y.append(1)
            else:
                y.append(0)
    return data
 
# 测试数据
labels('xss-200000.txt',x,1)
labels('good-xss-200000.txt',x,0)

# 训练模型
x_train, x_test, y_train, y_test = cross_validation.train_test_split(x,y, test_size=0.4, random_state=0)
clf = svm.SVC(kernel='linear', C=1).fit(x_train, y_train)
y_Predict = clf.predict(x_test)

# --- SVM验证 ---
test = [
	'AND 1=1',
	'ORDER BY 1-- ',
	'<script>alert(xss)</script>/',
	'and (select substring(@@version,1,1))=\'X\'',
	'www.baidu.com',
	'<?php @eval($_POST[\'c\']);?>'
]
# 数据向量化
z_test = []
for i in test:
	z_test.append( get_feature( i ) )

# 模型预测
z_pred = clf.predict(z_test)
mapvalues = {1:'Bad ',0:'Good'}
for i in range(len(z_test)):
	print( mapvalues[z_pred[i]] + ':' + test[i] )

# 保存训练模型
# joblib.dump(clf, "xss-svm-200000-module.m")
# 加载模型验证
# clf = joblib.load("xss-svm-200000-module.m")
# y_test = []
# y_test = clf.predict(x)
# print( metrics.accuracy_score(y_test,y) )




