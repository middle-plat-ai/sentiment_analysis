# -*- coding:utf-8 -*-


import os
import sys
sys.path.append('utils/')
from preprocess import *
from sentianalysis import *


main_path = os.path.abspath('.')
dict_path = main_path + '/dict/'


#修改各词库的路径
stopword_path = dict_path + 'stop_words.txt'
degreeword_path = dict_path + 'degreewords.txt'
sentimentword_path = dict_path + 'sentiment_word_score.txt'
deny_path = dict_path + 'denial_dict.txt'

# 停用词列表
stopwords = load_data(stopword_path)
#否定词表
notword = load_data(deny_path)
#程度词表
degree_dict = file2dict(degreeword_path)
#情感词表
sentiment_dict = file2dict(sentimentword_path)


text = '不太好吃，相当难吃，要是米饭再多点儿就好了'
# text = "剁椒鸡蛋好咸,土豆丝很好吃"
print('句子：%s的情感值为：%.4f' % (text, sents_score(text, sentiment_dict, degree_dict, notword)))