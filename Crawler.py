from selenium import webdriver
from time import sleep

url = ('https://www.snap.com/en-US/jobs/')
driver = webdriver.Chrome("C:\drivers\chromedriver.exe")
driver.get(url)

sleep(10)
html = driver.page_source
print(html)
with open("snap.html", "wb") as fh:
    fh.write(html.encode())
driver.quit()
