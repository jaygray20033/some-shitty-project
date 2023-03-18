from os import system
from matplotlib import image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from datetime import date
from datetime import datetime
import urllib.request
import os
system("cls")
system("COLOR 0A")
import time
usleep = lambda x: time.sleep(x/1000000.0)


options = webdriver.ChromeOptions()
# options.add_argument("--incognito")
# options.add_argument("--headless")
# options.add_argument("user-data-dir=C:\\Users\\Quýt\\AppData\\Local\\Google\\Chrome\\User Data")
web = webdriver.Chrome(executable_path="./Chrome/chromedriver.exe",options=options)
web.get("https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990")
system("cls")
key = input("Nhập key cần tìm kiếm: ")

path = "./image/"+ key
os.mkdir(path)
path = '''document.querySelector("body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input").value="'''+ key+'"'
web.execute_script(path)
sleep(1)
web.execute_script('''document.querySelector("body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > button > div").click()''')
count  = int(input("Số lượng bao nhiêu: "))
for i in range(1,count+1):
    img =  web.find_element('xpath','//*[@id="islrg"]/div[1]/div['+str(i)+ ']/a[1]/div[1]/img')
# # //*[@id="islrg"]/div[1]/div[213]/a[1]/div[1]/img
    url = img.get_attribute('src')
    path = "./image/"+key+'/'+ str(i)+".jpg"
    urllib.request.urlretrieve(url,path)
    
web.quit
print("Đã tải xong")