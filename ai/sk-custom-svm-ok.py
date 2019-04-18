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
from sklearn import metrics


# 判断特征维度
def get_evil_char(url):
	# 判断恶意字符的出现的个数，做为一个维度
    return len(re.findall("[<>,\'\"()/]", url, re.IGNORECASE))

def get_evil_word(url):
	# 判断恶意函数的出现的个数，做为一个维度
    return len(re.findall("(alert)|(script=)|(eval)|(src=)|(prompt)",url,re.IGNORECASE))

Dimensions = ["A", "N", "Z"]   # A-<	N->	  Z-代表各种html标签;判断这个三个维度
def labels(Data):
	#把参数泛化, 并获取词频
	preData = []		#泛化后，数据
	preCount = []		#泛化后，字母出现的次数;词频矩阵
	for i in Data:
		tt = i.replace("<", "A")
		tt = tt.replace(">", "N")
		tt = tt.replace("script", "Z")
		preData.append(tt)
		preCount.append([tt.count("A"), tt.count("N"), tt.count("Z")])
	return preCount, preData

# 预测结果百分比
def do_metrics(y_test,y_pred):
    print( "metrics.accuracy_score:" )
    print( metrics.accuracy_score(y_test, y_pred) )
    print( "metrics.confusion_matrix:" )
    print( metrics.confusion_matrix(y_test, y_pred) )
    print( "metrics.precision_score:" )
    print( metrics.precision_score(y_test, y_pred) )
    print( "metrics.recall_score:" )
    print( metrics.recall_score(y_test, y_pred) )
    print( "metrics.f1_score:" )
    print( metrics.f1_score(y_test,y_pred) )

# 测试数据
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

xss_list, xss_data = labels(badCase)  		# xss_list 为xss通过词频泛化出的一个词频矩阵； xss_data为泛化后的数据
safe_list, safe_data = labels(goodCase)
x = xss_list + safe_list

# 打上结果标记
safe_lable = [0 for i in range(0,len(goodCase))]
xss_lable = [1 for i in range(0,len(badCase))]		# 黑名单数据打上1的标记
y = xss_lable + safe_lable 


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
X_predict, X_data = labels(test)
# 模型预测
y_Predict = clf.predict(X_predict)
mapvalues = {1:'Bad ',0:'Good'}
for i in range(len(X_predict)):
	print( mapvalues[y_Predict[i]] + ':' + test[i] )

# 保存训练模型
# joblib.dump(clf, "xss-svm-200000-module.m")
# 加载模型验证
# clf = joblib.load("xss-svm-200000-module.m")
# y_test = []
# y_test = clf.predict(x)
# print( metrics.accuracy_score(y_test,y) )

