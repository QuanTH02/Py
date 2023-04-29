from selenium.webdriver.common.by import By
from selenium import webdriver

# Khởi tạo trình duyệt
driver = webdriver.Chrome()

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

driver.get(url)

row = driver.find_element(By.XPATH, '//*[@id="main"]/div/span/div/div/div[3]/table/tbody')

print(len(row))

driver.quit

