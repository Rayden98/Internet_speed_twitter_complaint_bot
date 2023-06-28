from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s = Service('C:/Users/MINED/Documents/Programs/chromedriver.exe')

driver = webdriver.Chrome(service=s)
speed_download = None
speed_upload = None
twitter_email = ""
twitter_password = ""
twitter_username = ""

def post_twitter():
    global speed_download, speed_upload

    post = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
    post.send_keys(f"Hey @iai0000 whi is my internet speed {speed_download}down/{speed_upload}up when I pay for 30down/10up in Maryland #speedtest ")
    time.sleep(5)

    button_post = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]')
    button_post.click()
    time.sleep(10)

def get_twitter():
    driver.get("https://twitter.com/i/flow/login?lang=en")

    time.sleep(15)

    email = driver.find_element(By.CLASS_NAME, "r-30o5oe")
    email.send_keys(twitter_email)

    time.sleep(5)

    next1 = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
    next1.click()

    time.sleep(5)

    try:
        username = driver.find_element(By.NAME, "text")
        username.send_keys(twitter_username)

        next2 = driver.find_element(By.XPATH,
                                    '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
        next2.click()
        time.sleep(5)

        password = driver.find_element(By.NAME, "password")
        password.click()
        password.send_keys(twitter_password)

        next3 = driver.find_element(By.XPATH,
                                    '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        next3.click()
    except:
        password = driver.find_element(By.NAME, "password")
        password.click()
        password.send_keys(twitter_password)

        next3 = driver.find_element(By.XPATH,
                                    '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        next3.click()
    time.sleep(10)

    post_twitter()

def get_speed():
    global speed_download, speed_upload
    driver.get("https://www.speedtest.net/")

    time.sleep(5)

    go = driver.find_element(By.CLASS_NAME, "start-text")
    go.click()

    time.sleep(50)

    download = driver.find_element(By.CLASS_NAME, "download-speed")
    speed_download = download.text

    upload = driver.find_element(By.CLASS_NAME, "upload-speed")
    speed_upload = upload.text

    get_twitter()



get_speed()



time.sleep(60)

driver.quit()
