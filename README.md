# sentiment_analysis

1 基于情感词典的情感极性分析

主体文件：sentianalysis.py

sents_score(text, sentiment_dict, degree_dict, notword)

text:需要计算情感的文本，可以是一个句子，也可以是多个句子

sentiment_dict：情感词典，包含情感词，及其对应的分值

degree_dict：程度词典，包含程度词，及其对应的分值

notword：否定词

demo.py是一个运行的例子

运行
python demo.py
