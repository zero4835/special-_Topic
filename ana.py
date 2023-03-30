import jieba
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from snownlp import SnowNLP

# 要進行情感分析的中文文本
text = "這裡的風景很美。"

# 使用jieba庫對文本進行分詞
words = jieba.cut(text)

# 將分詞結果轉換為列表
words_list = list(words)

# 初始化情感分析器
sid = SentimentIntensityAnalyzer()

# 將分詞結果列表轉換為字符串
text = " ".join(words_list)

# 使用NLTK庫進行情感分析
scores = sid.polarity_scores(text)

# 打印情感分數
print("原文本：",text)
print("情感分數：", scores)

# 初始化情感分析器
s = SnowNLP(text)

# 打印情感分數
print("原文本：", text)
print("情感分數：", s.sentiments)