
import pandas as pd
import softmax as sm
import gradingtransfer as gs

userID = ["1", "2", "3", "4", "5"]
location = ["Taichung", "Taipei", "Hsinchu", "Kaohsiung", "Taoyuan"]

def writeExcel(text, user, location):
    #load excel
    df = pd.read_csv('C:/Users/ROUSER6/Desktop/topic/ana/excel/test.csv')
    
    #counting sentiment and score
    sentiment, score = gs.determineSentiment(sm.emotion_score(text))
    
    data = {"UserID": user, "Sentimet": sentiment, "Score": score, "Location" : location}
    df = pd.DataFrame(data, index=[0])
    #df.to_excel('./test.xlsx', index=False)
    
    
    try:
        old_data = pd.read_excel('C:/Users/ROUSER6/Desktop/topic/ana/excel/test.xlsx')
    except FileNotFoundError:
        #若沒有建立新資料
        old_data = pd.DataFrame()

    # merge new and old data into excel
    merged_data = pd.concat([old_data, df], ignore_index=True)
 
    #write back excel
    merged_data.to_excel('C:/Users/ROUSER6/Desktop/topic/ana/excel/test.xlsx', index=False)

text1 = '這本書真是太棒了！'
text2 = '這個產品有點失望，跟預期的不太一樣'
text3 = '今天天氣還不錯，我在公園裡散步'
text4 = '望月峰獻堂登山步道非常好走，如果平常有在運動可能會覺得不算什麼！沒有在運動的人可以就當作健行～隨著慢慢走上山，就可以到月峰景平台眺望整個大台中的風景！跟三五好友揪團去爬還可以趁機請對方拍美照！不管是早上或是夕陽西下都能拍到不錯的好照片～如果想要散步，夜晚到這裡走走，也是不錯的好選擇。'
text5 = '幻覺博物館最早起源自克羅埃西亞，利用視覺錯位產生的各種幻覺，令觀者不敢相信眼前所見到底是真是假，也因此成為風靡全球的新打卡景點，而在2020年幻覺博物館也終於落地台中，運用鏡子、幾何等道具混淆你的視覺感官！想挑戰與眾不同的博物館嗎？快揪朋友們一起到幻覺博物館拍更多奇特又有趣的照片吧！'
text6 = '日日旅海外面還有個大草坪上面有一台可愛的小餐車住客可以免費兌換任何品項有冰淇淋、氣泡飲、咖啡☕️🍦如果只是一般遊客在營業時間入場費90 可以抵消費有去墾丁走走很推這個位在滿州鄉的民宿遠離塵囂，非常靜謐又放鬆～💖💖' 
text7 = '今年大棠紅葉🍁特別靚特別多由9:30am開始上山到3:30pm才下到山🏃🏻‍♀️全個元朗大擠塞人山人海好似行年宵咁誇張👯‍♀️👯👯‍♂️👯‍♀️👯👯‍♂️👯‍♀️👯👯‍♂️￼￼我哋去景點￼「楓香林￼」遊覽打卡波波車一身牛仔打扮成為流動景點被打卡￼基本上六個鐘頭有四個鐘頭都係背住波波今日負重7kg行山運動6小時￼絕對是體力耐力嘅堅持同配合🏋️‍♀️玩得開心￼影到靚相都係值得￼🥰'
text8 = '無邊際觀景平台，可以眺望美麗夕陽和海景，也可以騎腳踏車享受微風吹拂，假日來走走散步很愜意呢～'
text9 = '點了豬油拌面 跟五香肉燥，豬油拌面本應該要有豬油香氣 完全沒有，原本以為味覺壞掉叫了女朋友來吃 也是相同反應 令人失望'

writeExcel(text1, userID[0], location[0])
writeExcel(text2, userID[1], location[1])
writeExcel(text3, userID[2], location[2])
writeExcel(text4, userID[3], location[3])
writeExcel(text5, userID[4], location[4])
writeExcel(text6, userID[4], location[4])
writeExcel(text7, userID[4], location[4])
writeExcel(text8, userID[4], location[4])
writeExcel(text9, "D1528587", location[1])
