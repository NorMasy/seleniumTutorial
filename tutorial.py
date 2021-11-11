import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#
# change download directory
downloadPath = Options ()
downloadPath.add_experimental_option("prefs", {"download.default_directory" : "D:\\"})
#
# get web browser driver
driverChrome = webdriver.Chrome("C:\\Users\\norma\\Downloads\\selenium\\chromedriver_win32\\chromedriver.exe", options = downloadPath)
#

# implicitly wait
driverChrome.implicitly_wait(30)
#
# go to the website
driverChrome.get("https://www.ilovepdf.com/")
#
# maximize the window
driverChrome.maximize_window()
#
# find merge pdf
target = driverChrome.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/a")
#
time.sleep(2)
#
target.click()
#
# upload (select first pdf file)
upload = driverChrome.find_element_by_xpath("/html/body/div/div/div/div/div/input")

time.sleep(2)

# path of file to be upload
upload.send_keys("D:\\Pdf 1.pdf")
#
time.sleep(3)
#
# upload (2nd pdf file)
upload2 = driverChrome.find_element_by_xpath("/html/body/div/div/div/div/div/div/input")
#
# path of file to be upload
upload2.send_keys("D:\\Pdf 2.pdf")

#
time.sleep(2)

# merge
merge = driverChrome.find_element_by_xpath("/html/body/div/div/button").click()
# merge = driverChrome.find_element_by_id("processTask").click()
#
# # download
# download = driverChrome.find_element_by_id("pickfiles")
#
#
#
