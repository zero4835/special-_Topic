import pandas as pd
import jieba, thulac
import time

df=pd.read_excel("./convert_segment.xlsx")
df=df[['詞語', '詞性種類', '詞意數', '情感分類', '強度', '極性']]
df.head()

Happy=[]
Good=[]
Surprise=[]
Anger=[]
Sad=[]
Fear=[]
Disgust=[]

for idx, row in df.iterrows():
    if row['情感分類'] in ['PA', 'PE']:
        Happy.append(row['詞語'])
    if row['情感分類'] in ['PD', 'PH', 'PG', 'PB', 'PK']:
        Good.append(row['詞語'])
    if row['情感分類'] in ['PC']:
        Surprise.append(row['詞語'])
    if row['情感分類'] in ['NA']:
        Anger.append(row['詞語'])
    if row['情感分類'] in ['NB', 'NJ', 'NH', 'PF']:
        Sad.append(row['詞語'])
    if row['情感分類'] in ['NI', 'NC', 'NG']:
        Fear.append(row['詞語'])
    if row['情感分類'] in ['NE', 'ND', 'NM', 'NK', 'NL']:
        Disgust.append(row['詞語'])
        
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
    
    #過濾重複字詞
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

show=emotion_caculate("主打浮誇系餐點的難吃的森川丼丼，不只有來這必點的爆蝦霸王船，還有森川滿貫列車及排山倒海丼都不能錯過，從新鮮度到餐點的精緻度都讓人印象深刻,在GOOGLE評論上更是高達4.7顆星,近期更是將營業時段改為早上11點至凌晨12點,從中午到宵夜都能吃得到簡直太幸福~還沒吃過的你一定要收藏起來啦！")
print(show)