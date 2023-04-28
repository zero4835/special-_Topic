from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import requests
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


##兩個txt檔都先幫你清空了


# 你的資訊
url = "https://www.facebook.com/"
url2="https://www.facebook.com/emuse.com.tw"
email = "cyclone4835@yahoo.com.tw" 
password = "Zjasxwww6633"



chrome_options = webdriver.ChromeOptions()
prefs = {
    "profile.default_content_setting_values.notifications": 2
}
chrome_options.add_experimental_option("prefs", prefs)

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=chrome_options)
    


# 最大化視窗
driver.maximize_window()
# 進入Facebook登入畫面
driver.get(url)

# 填入帳號密碼，並送出
driver.find_element("id", "email").send_keys(email)
driver.find_element("id", "pass").send_keys(password)
driver.find_element("name", "login").click()



time.sleep(5)

# 進入連結
driver.get(url2)

time.sleep(5)



#處裡顯示更多   
def openSeeMore(driver):
    readMore = driver.find_elements(By.XPATH, "//div[contains(@class,'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f') and contains(text(), '顯示更多')]")
    if len(readMore) > 0:    
        count = 0
        for i in readMore:
            action=ActionChains(driver)
            try:
                action.move_to_element(i).click().perform()
                count += 1
            except:
                try:
                    driver.execute_script("arguments[0].click();", i)
                    count += 1
                except:
                    continue
        if len(readMore) - count > 0:
            print('readMore issue:', len(readMore) - count)
        time.sleep(1)
    else:
        pass


# 往下滑3次，讓Facebook載入文章內容
for x in range(3):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    print("scroll")
    time.sleep(5) #要設時間給fb緩衝載入資料
    openSeeMore(driver)


root = BeautifulSoup(driver.page_source, "html.parser")


#尋找貼文
titles = root.find_all(
    "div", class_="xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a")

#尋找發文者和打卡地點
infos=root.find_all(
    class_="x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz x1gslohp x1yc453h"
)

with open("location.txt", 'r+') as f: #清除發文者及打卡地點txt檔
    f.truncate(0)


with open("posts.txt", 'r+') as f: #清除貼文txt檔
    f.truncate(0)

with open("final.txt", 'r+') as f: #清final txt檔
    f.truncate(0)

#爬出發文者及打卡地點 然後寫入txt


locations=[]
for info in infos:
    locations.append(info.text)
    
    



#爬出貼文 然後寫入txt
postpage=0
p=[]
hashtag=[[0]*100 for i in range(100)]
for title in titles:
    # 定位每一行標題
    posts = title.find_all("div", dir="auto")
    # 如果有文章標題才印出
    if len(posts):
        str1=''
        for post in posts:
            str1=str1+post.text+'\n'
            str3=post.text+'\n'
            if post.text.find('#')>=0: # 若有讀取到 # 則進入迴圈
               
                loc=post.text.find('#') # 紀錄#在第幾個字元
                h=0
                str2='' #存放hashtag 的字串
                for i in range(loc + 1, len(str3)): 
                    if(str3[i]=='#'or str3[i]=='\n' or str3[i]==' '): # 檢測是否讀取到下一個 # 或換行 或空格
                        
                        hashtag[postpage].append(str2) #將字串存進陣列中
                        h=h+1
                        
                        str2=''#清空存放 hashtag的字串
                    else:
                        str2= str2+str3[i]
        p.append(str1)
 
    postpage+=1


file = open("final.txt", mode = "a", encoding = "utf-8")
for i in range(postpage):
    file.write("this is post No: ")
    file.write(str(i+1)) #貼文編號
    file.write("\n")
    file.write("\n")
    file.write(locations[i])#發文者及打卡地點
    file.write("\n")
    file.write("\n")
    file.write(p[i])  #貼文內容
    file.write("\n")
    file.write("\n")
    file.write("this are hashtag: ")
    file.write("\n")
    for j in range(100,len(hashtag[i])):
        file.write(str(hashtag[i][j]))  # hashtags
        file.write("\n")
    file.write("-"*50)
    file.write("\n") 
file.close
time.sleep(5)
driver.quit()

