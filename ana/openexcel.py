import pandas as pd
import jieba, thulac
import time

df=pd.read_excel("./convert_segment.xlsx")

df = df[['词语', '词性种类', '词义数', '词义序号', '情感分类', '强度', '极性']]
df.head()

Happy=[]
Good=[]
Surprise=[]
Anger=[]
Sad=[]
Fear=[]
Disgust=[]

for idx, row in df.iterrows():
    if row['情感分类'] in ['PA', 'PE']:
        Happy.append(row['词语'])
    if row['情感分类'] in ['PD', 'PH', 'PG', 'PB', 'PK']:
        Good.append(row['词语']) 
    if row['情感分类'] in ['PC']:
        Surprise.append(row['词语'])     
    if row['情感分类'] in ['NA']:
        Anger.append(row['词语'])    
    if row['情感分类'] in ['NB', 'NJ', 'NH', 'PF']:
        Sad.append(row['词语'])
    if row['情感分类'] in ['NI', 'NC', 'NG']:
        Fear.append(row['词语'])
    if row['情感分类'] in ['NE', 'ND', 'NN', 'NK', 'NL']:
        Disgust.append(row['词语'])
        
Positive = Happy + Good +Surprise
Negative = Anger + Sad + Fear + Disgust
print('情绪词语列表整理完成') 

Positive=Happy+Good+Surprise
Negative=Anger+Sad+Fear+Disgust

def emotion_caculate(text):
    positive = 0
    negative = 0
    anger = 0
    disgust = 0
    fear = 0
    sad = 0
    surprise = 0
    good = 0
    happy = 0
    
    wordlist = jieba.lcut(text)
    
    #thu = thulac.thulac(seg_only=True)
    #words = thu.cut(text)
    
    #wordlist=[]
    #for word, tag in words:
        #if word!=',':
            #wordlist+=word
    
    #���瞈暸��銴�摮�閰�
    wordset = set(wordlist)
    
    wordfreq = []
    for word in wordset:
        print(" ", word, end='')
        freq = wordlist.count(word)
        if word in Positive:
            positive+=freq
        if word in Negative:
            negative+=freq
        if word in Anger:
            anger+=freq
        if word in Disgust:
            disgust+=freq
        if word in Fear:
            fear+=freq
        if word in Sad:
            sad+=freq
        if word in Surprise:
            surprise+=freq
        if word in Good:
            good+=freq
        if word in Happy:
            happy+=freq
    emotion_info = {
        'length':len(wordlist),
        'positive': positive,
        'negative': negative,
        'anger': anger,
        'disgust': disgust,
        'fear':fear,
        'good':good,
        'sadness':sad,
        'surprise':surprise,
        'happy':happy,
    }
    indexs = ['length', 'positive', 'negative', 'anger', 'disgust','fear','sadness','surprise', 'good', 'happy']
    return (pd.Series(emotion_info, index=indexs))

show=emotion_caculate("銝餅��瘚株��蝟駁��暺�������������璉桀��銝潔蜈嚗�銝���芣��靘����敹�暺���������阡�貊����對��������璉桀��皛輯疵���頠�������撅勗��瘚瑚蜈��賭����賡�舫��嚗�敺���圈悅摨血�圈��暺����蝎曄溶摨阡�質��鈭箏�啗情瘛勗��,��沁OOGLE閰�隢�銝���湔�舫�����4.7憿����,餈������湔�臬�����璆剜��畾菜�寧�箸�拐��11暺���喳�����12暺�,敺�銝剖����啣挾憭���質�賢��敺���啁陛��游云撟貊��~���瘝����������雿�銝�摰�閬���嗉��韏瑚����佗��")
print(show)