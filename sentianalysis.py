# -*- coding:utf-8 -*-

from pyhanlp import *
import sys
sys.path.append('utils/')
from preprocess import *


"""
step 1 : 分词且去除停用词
"""
def sent2wordloc(sentence):
    #wordlist = [word for word in jieba.cut(sentence) if word not in stopwords]
    sentence = Traditional2Simplified(sentence.lower())
    wordlist = [str(word).split('/', 1)[0] for word in HanLP.segment(sentence)]
    wordloc = {wordlist[i]: i for i in range(len(wordlist))}
    return wordlist, wordloc

"""
step 2 : 针对分词结果，定位情感词、否定词及程度词
"""
def wordclassify(sentence, sentiment_dict, degree_dict, notword):
    wordlist, wordloc = sent2wordloc(sentence)
    sentimentloc, notloc, degreeloc, othersloc = {}, {}, {}, {}
    for i in range(len(wordlist)):
        word = wordlist[i]
        if word in sentiment_dict.keys() and word not in notword and word not in degree_dict.keys():
            sentimentloc[i] = sentiment_dict[word]
        elif word in notword and word not in degree_dict.keys():
            notloc[i] = -1
        elif word in degree_dict.keys():
            degreeloc[i] = degree_dict[word]
        else:
            othersloc[i] = 0
    #sentimentloc = sorted(sentimentloc.items(), key=lambda x:x[0],reverse=False)
    return sentimentloc, notloc, degreeloc, othersloc, wordlist, wordloc

"""
step 3 : 情感打分
"""
def sent_score(sentence, sentiment_dict, degree_dict, notword):
    sentimentloc, notloc, degreeloc, othersloc, wordlist, wordloc = wordclassify(sentence, sentiment_dict, degree_dict, notword)
    sentimentloc = dict(sorted(sentimentloc.items(), key=lambda x: x[0], reverse=False))
    score = 0
    keys = list(sentimentloc.keys())
    for i in range(len(keys)):
        w = 1
        index = keys[i]

        j_no = -1
        j_fu = -1

        if i == 0:
            for j in range(keys[0]):
                if j in notloc.keys():
                    w *= -1
                    j_no = j

                elif j in degreeloc.keys():
                    w *= float(degreeloc[j])
                    j_fu = j

        else:
            for j in range(keys[i - 1] + 1, keys[i] + 1):
                if j in notloc.keys():
                    w *= -1
                    j_no = j

                elif j in degreeloc.keys():
                    w *= float(degreeloc[j])
                    j_fu = j

        if j_no > j_fu and j_no != -1 and j_fu != -1:
            score += w * float(sentiment_dict[wordlist[index]]) * 1.25
        elif j_no < j_fu and j_no != -1 and j_fu != -1:
            score += w * float(sentiment_dict[wordlist[index]]) * 0.75 / (float(degree_dict[wordlist[j_fu]]))
        else:
            score += w * float(sentimentloc[keys[i]])
    return score

###如果句子中含有多个句子，需要先分句，计算每个句子的情感分值，再取均值；
cutlist = """
。.！!？?；;……\n\r
"""

sents_cut = SentenceCut()

def sents_score(text, sentiment_dict, degree_dict, notword):
    if text != '':
        sents = sents_cut.cut_sents(cutlist, text)
        scores = 0
        counts = 0
        for sentence in sents:
            score = sent_score(sentence, sentiment_dict, degree_dict, notword)
            if score != 0:
                scores +=score
                counts +=1
        if counts == 0:
            return 0
        else:
            return scores / counts
    else:
        return 0


