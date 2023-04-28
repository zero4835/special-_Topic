from snownlp import SnowNLP
import math
import testopen as to
import thulac
import sys
import jieba


#make each line in the file in the list
def loadTxt(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            lines.append(line)
            line = f.readline()
    return lines

# thulac init
thu = thulac.thulac()

# slef define break_word_dict
jieba.load_userdict('C:/Users/ROUSER6/Desktop/topic/ana/dict_define.txt')

#count emtion score 
def emotion_score(text):
    print("--------------------------\n")
    #words = thu.cut(text)
    #去除標點符號
    #words = [word[0] for word in words if word[1] != 'w']
    
    #break word
    words = jieba.cut(text)
    
    #score_init
    score = [0, 0, 0] # 負面, 中立, 正面 
    flag=0
    
    print(text)
    
    positive = loadTxt('C:/Users/ROUSER6/Desktop/topic/ana/NTUSD_traditional/NTUSD_positive.txt')
    negative = loadTxt('C:/Users/ROUSER6/Desktop/topic/ana/NTUSD_traditional/NTUSD_negative.txt')
    #positive = lazy_load('./testpos.txt')
    #negative = lazy_load('./testneg.txt')
    
    for word in words:
        #remove space
        word=word.strip()
        #print(word)
        flag=0
        
        for pos in positive:
            pos=pos.strip()
            if word == pos:
                score[2] += 1
                flag=1
                break
            
        for neg in negative:
            neg=neg.strip()
            
            if neg == word:
                score[0] += 1
                flag=1
                break
            
        if flag!=1:
            score[1] += 0.001
            
    print(score[0], format(score[1], ".3f"), score[2]) # 負面, 中立, 正面    
    
    # 進行softmax轉換
    exp_scores = [math.exp(i) for i in score]
    softmax_scores = [round(j / sum(exp_scores), 2) for j in exp_scores]
    return {"neg":softmax_scores[0], "neu":softmax_scores[1], "pos":softmax_scores[2]}

# 測試
# text1 = '這本書真是太棒了！'
# text2 = '這個產品有點失望，跟預期的不太一樣'
# text3 = '今天天氣還不錯，我在公園裡散步'
# text4 = '望月峰獻堂登山步道非常好走，如果平常有在運動可能會覺得不算什麼！沒有在運動的人可以就當作健行～隨著慢慢走上山，就可以到月峰景平台眺望整個大台中的風景！跟三五好友揪團去爬還可以趁機請對方拍美照！不管是早上或是夕陽西下都能拍到不錯的好照片～如果想要散步，夜晚到這裡走走，也是不錯的好選擇。'
# text5 = '幻覺博物館最早起源自克羅埃西亞，利用視覺錯位產生的各種幻覺，令觀者不敢相信眼前所見到底是真是假，也因此成為風靡全球的新打卡景點，而在2020年幻覺博物館也終於落地台中，運用鏡子、幾何等道具混淆你的視覺感官！想挑戰與眾不同的博物館嗎？快揪朋友們一起到幻覺博物館拍更多奇特又有趣的照片吧！'
# text6 = '日日旅海外面還有個大草坪上面有一台可愛的小餐車住客可以免費兌換任何品項有冰淇淋、氣泡飲、咖啡☕️🍦如果只是一般遊客在營業時間入場費90 可以抵消費有去墾丁走走很推這個位在滿州鄉的民宿遠離塵囂，非常靜謐又放鬆～💖💖' 
# text7 = '今年大棠紅葉🍁特別靚特別多由9:30am開始上山到3:30pm才下到山🏃🏻‍♀️全個元朗大擠塞人山人海好似行年宵咁誇張👯‍♀️👯👯‍♂️👯‍♀️👯👯‍♂️👯‍♀️👯👯‍♂️￼￼我哋去景點￼「楓香林￼」遊覽打卡波波車一身牛仔打扮成為流動景點被打卡￼基本上六個鐘頭有四個鐘頭都係背住波波今日負重7kg行山運動6小時￼絕對是體力耐力嘅堅持同配合🏋️‍♀️玩得開心￼影到靚相都係值得￼🥰'
# text8 = '無邊際觀景平台，可以眺望美麗夕陽和海景，也可以騎腳踏車享受微風吹拂，假日來走走散步很愜意呢～'
# text9 = '點了豬油拌面 跟五香肉燥，豬油拌面本應該要有豬油香氣 完全沒有，原本以為味覺壞掉叫了女朋友來吃 也是相同反應 令人失望'

# print(emotion_score(text1)) # [0.96, 0.01, 0.03]
# print(emotion_score(text2)) # [0.02, 0.05, 0.93]
# print(emotion_score(text3)) # [0.07, 0.88, 0.05]
# print(emotion_score(text4))
# print(emotion_score(text5))
# print(emotion_score(text6))
# print(emotion_score(text7))
# print(emotion_score(text8))


# #if word in positive:
#             score[0] += 1
#         elif word in negative:
#             score[2] += 1
#         else:
#             score[1] += 1