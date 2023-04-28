from snownlp import SnowNLP
import thulac
import jieba
import open_dic as od

thu = thulac.thulac(seg_only=True)

# 要進行情感分析的中文文本
text = "龍山寺附近餐廳的菜色非常難吃，服務也非常周到，價格也相當實惠。"\
"我很喜歡這裡的環境，氣氛很不錯。而北埔則是客家擂茶很好喝，北埔"\
"也很棒"
      
words = thu.cut(text)
#words=jieba.cut(text, cut_all =False)
score = 0

for word, tag in words:
    #去除空白
    word=word.strip()
    if word!='，'  and word!='.' and word!='！' and word!='?' and word!='的' and word!='很' and word!='真' and word!='啦':
        print(word)
        score += od.open_pos(word)
        score += od.open_neg(word)

# 輸出結果
if score > 0:
    print('正面情緒')
elif score < 0:
    print('負面情緒')
else:
    print('中立情緒',)
    
print(text)    
print(score)
