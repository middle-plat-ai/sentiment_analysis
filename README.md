# sentiment_analysis

## 情感分析资料

[sentiment_analysis(English)](https://github.com/sebastianruder/NLP-progress/blob/master/english/sentiment_analysis.md)

[awesome-sentiment-analysis](https://github.com/xiamx/awesome-sentiment-analysis)

[baidu/Senta](https://github.com/baidu/Senta)

[snownlp](https://github.com/isnowfy/snownlp)

[AllenNLP senttiment_analysis](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2650750932&idx=3&sn=30b8412c4d612f52ae5f0c42ae001b07&chksm=871afbaab06d72bc110e2c73eb70b56d5b56acf98faa4bd5f94f5c8cfc91c4e894e5b9c16597&scene=21#wechat_redirect)

## 1 基于情感词典的情感极性分析

  ### 主体文件：sentianalysis.py

    sents_score(text, sentiment_dict, degree_dict, notword)

    text:需要计算情感的文本，可以是一个句子，也可以是多个句子

    sentiment_dict：字典，情感词典，包含情感词，及其对应的分值

    degree_dict：字典，程度词典，包含程度词，及其对应的分值

    notword：列表，否定词

  ### 简单用例

  运行

    python demo.py

  会得到如下结果：

    还可以，比预计时间晚了一小时到，不过还好

    情感分值：-0.6789
