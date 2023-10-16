from selenium import webdriver

chrome_driver_path = 'c:\Program Files\Google\Chrome\Application\chrome.exe'
url = "https://www.youtube.com/"
driver = webdriver.Chrome()
driver.get(url)
driver.quit()





