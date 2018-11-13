# sentiment_analysis

情感分析资料：

[awesome-sentiment-analysis](https://github.com/xiamx/awesome-sentiment-analysis)

[baidu/Senta](https://github.com/baidu/Senta)

[snownlp](https://github.com/isnowfy/snownlp)

1 基于情感词典的情感极性分析

主体文件：sentianalysis.py

sents_score(text, sentiment_dict, degree_dict, notword)

text:需要计算情感的文本，可以是一个句子，也可以是多个句子

sentiment_dict：情感词典，包含情感词，及其对应的分值

degree_dict：程度词典，包含程度词，及其对应的分值

notword：否定词

demo.py是一个运行的例子

直接运行

python demo.py

会得到如下结果：

还可以，比预计时间晚了一小时到，不过还好的情感值为：-0.6789
