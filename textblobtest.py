import jieba
from textblob import TextBlob
import thulac
from snownlp import SnowNLP

def analyze_sentiment(post):
    # 使用jieba分詞
    words = jieba.cut(post)
    # 定義情緒值和情緒詞數
    sentiment = 0
    count = 0
    # 使用TextBlob分析情緒
    blob = TextBlob(post)
    sentiment += blob.sentiment.polarity
    count += 1
    # 使用THULAC分析情緒
    thu = thulac.thulac()
    thu_sentiment = thu.cut(post, text=True)
    thu_blob = TextBlob(thu_sentiment)
    sentiment += thu_blob.sentiment.polarity
    count += 1
    # 使用SnowNLP分析情緒
    snow = SnowNLP(post)
    sentiment += snow.sentiments
    count += 1
    # 計算平均情緒值
    if count > 0:
        sentiment /= count
    # 根據情緒值判斷情緒
    if sentiment > 0:
        print("這篇貼文情緒正向！")
    elif sentiment < 0:
        print("這篇貼文情緒負向！")
    else:
        print("這篇貼文情緒中立！")
    # 回傳情緒值
    return sentiment

post = "[九份] 遊記分享！今天來到 [九份]，一進門就被這裡的美不勝收景色吸引了！緊接著，我參加了 [九份] 的 [體驗活動]，感覺非常興奮！而且，這裡的 [美食或飲料] 真的很 [美味]，尤其是 [著名的美食或飲料]，一定要嚐嚐！總之，我對這次的 [九份] 之旅非常滿意，真心推薦給大家！ #旅遊 #打卡 #探索 #[九份]"
test="逢甲不美麗，也不有趣，讓我很難過"
analyze_sentiment(test)