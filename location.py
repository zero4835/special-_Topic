import jieba
import jieba.posseg as pseg
from snownlp import SnowNLP
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import thulac

thu = thulac.thulac(seg_only=True)

# 要進行情感分析的中文文本
test = "龍山寺附近餐廳的菜色非常吃，服務也非常周到，價格也相當實惠。"\
"我很喜歡這裡的環境，氣氛很不錯。而北埔則是客家擂茶很好喝，北埔"\
"也很棒"

test2="新開幕HOME燒肉吃到飽599元起！安格斯牛、戰斧豬排、大生蠔、"\
"火鍋、蓋飯、甜點、飲料、哈根達斯、HERSHEY'S冰沙無限供應。"

test3="這裡不美麗，也不有趣"

test4="主打浮誇系餐點的難吃的森川丼丼，不只有來這必點的爆蝦霸王船，還有森川滿貫列車及排山倒海丼都不能錯過，"\
      "從新鮮度到餐點的精緻度都讓人印象深刻，在GOOGLE評論上更是高達4.7顆星，近期更是將營業時段改為早"\
      "上11點至凌晨12點，從中午到宵夜都能吃得到簡直太幸福～還沒吃過的你一定要收藏起來啦！"
      
text=test4

# 使用jieba預設辭典對文本進行分詞
words = thu.cut(text)

# 初始化情感分析器
sentiments = []
# 初始化地點列表
locations = []

# 逐詞進行情感分析
for word, tag in words:
    # 判斷是否為地點詞
    if word!=',':
        text+=word+ " "
    if pseg.lcut(word)[0].flag == "ns":
        locations.append(word)
    else:
        # 使用 SnowNLP 進行情感分析
        s = SnowNLP(word)
        sentiment = s.sentiments
        print(word,sentiment)
        sentiments.append(sentiment)
        
        
def cntScore(sentiment, x):
    cnt=0
    sum=0
    avgScore=0
    
    for s in sentiments:
        if x==1:
            if s > 0.4:
                sum+=s  
        elif x==0:
            if s <= 0.4:
                sum+=s
        cnt+=1
    avgScore=sum/cnt
    return avgScore
            

#pos_score=cntScore(sentiments, 1)
#neg_score=cntScore(sentiments, 0)
# 計算情感分數
pos_score = sum([s for s in sentiments if s > 0.4])
neg_score = sum([s for s in sentiments if s <= 0.4])

score=0
if pos_score > neg_score:
    overall_sentiment = "正面"
    score=pos_score
elif pos_score < neg_score:
    overall_sentiment = "負面"
    score=neg_score
else:
    overall_sentiment = "中立"

#去除重複的地點
unique_location_words = list(set(locations))

# 打印結果
print("\n評論：", test4)
print("斷詞結果: ", text)
print("情感分數：", overall_sentiment, pos_score, neg_score)
print("斷詞後的地點：", unique_location_words)