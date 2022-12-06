import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import os

PATH = "C:\Program Files (x86)\chromedriver.exe"


def run_script(movie, link):

    download_path_main_folder = str(r'C:\Users\maina\OneDrive\Desktop\TikTok_Audios\Video_Clips')
    folder_name = movie

    final_download_path = os.path.join(download_path_main_folder, folder_name)
    if not os.path.exists(final_download_path):
        os.mkdir(final_download_path)

    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : final_download_path}
    chromeOptions.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(executable_path=PATH, options=chromeOptions)

    # website it goes too
    driver.get('https://www.videovor.com/en/downloader-online-f9')
    search = driver.find_element(by=By.ID, value="url")
    try:
        # first send keys is to the youtube video you want to download
        search.send_keys(link)
        search.send_keys(Keys.RETURN)

        driver.implicitly_wait(3)

        search2 = driver.find_element(by=By.ID, value='buttonDL')
        search2.click()

        driver.implicitly_wait(5)

        search3 = driver.find_element(by=By.ID, value='dlimg')
        search3.click()
        
        time.wait(5)
        driver.quit()
    except:
        print('error')