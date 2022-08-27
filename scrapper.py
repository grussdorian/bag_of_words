from selenium import webdriver  
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://www.youtube.com/watch?v=vfOk6nPUtIc')
driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/div[7]/div[1]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/yt-icon-button/button/yt-icon')
driver.find_elements(By.CLASS_NAME, 'segment-text style-scope ytd-transcript-segment-renderer')