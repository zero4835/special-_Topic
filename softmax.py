from snownlp import SnowNLP
import math
import testopen as to
import thulac
import sys

def lazy_load(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()

positive = lazy_load('./NTUSD_traditional/NTUSD_positive.txt')
negative = lazy_load('./NTUSD_traditional/NTUSD_negative.txt')


thu = thulac.thulac()

def emotion_score(text):
    words = thu.cut(text)
    #去除標點符號
    words = [word[0] for word in words if word[1] != 'w']
    
    score = [0, 0, 0] # 正面, 中性, 負面
    flag=0
    
    for word in words:
        word=word.strip()
        print(word)
        flag=0
        
        for pos in positive:
            pos=pos.strip()
            if word == pos:
                score[0] += 1
                flag=1
                break
        for neg in negative:
            neg=neg.strip()
            if neg == word:
                score[2] += 1
                flag=1
                break
        if flag!=1:
            score[1] += 1
    print(score[0], score[1], score[2]) # 負面, 中立, 正面    
    
    # 進行softmax轉換
    exp_scores = [math.exp(i) for i in score]
    softmax_scores = [round(j / sum(exp_scores), 2) for j in exp_scores]
    return softmax_scores

# 測試
text1 = '這本書真是太棒了！'
text2 = '這個產品有點失望，跟預期的不太一樣'
text3 = '今天天氣還不錯，我在公園裡散步'

#print(emotion_score(text1)) # [0.96, 0.01, 0.03]
print(emotion_score(text2)) # [0.02, 0.05, 0.93]
#print(emotion_score(text3)) # [0.07, 0.88, 0.05]
