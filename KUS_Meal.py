import time
import telegram
import datetime
from github import Github
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By

bot = telegram.Bot(token='**********************************************')
chat_id = -*************

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)
driver.get("https://sejong.korea.ac.kr/campuslife/facilities/dining/weeklymenu")
work = driver.find_element(By.XPATH,"//*[@id='sCont']/div[2]/p[2]/span/a[1]").click()
driver.switch_to.window(driver.window_handles[1])
url = driver.current_url
close = driver.quit()

with open ('Update_Date.txt', 'r+') as f_read :
    before = f_read.readline()
    if before != url :
        today = datetime.datetime.now() - timedelta(hours=-9)
        today_week = today.strftime('%Y-%m-%d')
        run = bot.sendMessage(chat_id = chat_id, text = "[DATE] " + today_week + '\n' + "[식단주소] " + url)
        repo = Github("****************************************").get_user().get_repo("Alarmbot_Meal")
        file = repo.get_contents('Update_Date.txt')
        repo.update_file('Update_Date.txt','',url,file.sha)
    f_read.close()
