# -*- coding: utf-8 -*-
# author: Bing
# email: wulitouhaha@vip.qq.com

import re
from sklearn.externals import joblib

# 判断特征维度
def get_evil_char(url):
	# 判断恶意字符的出现的个数，做为一个维度
    return len(re.findall("[<>,\'\"()/]", url, re.IGNORECASE))

def get_evil_word(url):
	# 判断恶意函数的出现的个数，做为一个维度
    return len(re.findall("(alert)|(script=)|(eval)|(src=)|(prompt)|(onerror)|(onload)|(onfocus)|(onmouseover)|(string.fromcharcode)|(document.cookie)|(%3c)|(%3e)|(%20)|(iframe)|(href)|(javascript)|(data)",url,re.IGNORECASE))

def get_feature(url):
    return [ get_evil_char(url), get_evil_word(url) ]

# 机器验证
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
clf = joblib.load("xss-svm-200000-module.m")
z_pred = clf.predict(z_test)
mapvalues = {1:'Bad ',0:'Good'}
for i in range(len(z_test)):
	print( mapvalues[z_pred[i]] + ':' + test[i] )

