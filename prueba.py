from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge("C:/Users/zheng\Downloads/edgedriver_win64/msedgedriver.exe")
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")



login = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]")
login.send_keys("zhengcarlos123@gmail.com")

time.sleep(1)

continueb = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[2]/span/span/input")
continueb.click()

password = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[1]/input")
password.send_keys("897579091.amazon")

sign = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[2]/span/span/input")
sign.click()

search = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
search.send_keys("HP Pavilion azul")

searchicon = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
searchicon.click()

Producturl = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span")
Producturl.click()

time.sleep(0.5)

elemento1 = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[9]/div[6]/div[1]/div[4]/div/div/div/div/div/form/div/div/div/div/div[3]/div/div[13]/div[1]/span/span/span/input")
elemento1.click()

search2 = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
search2.send_keys("HP Pavilion azul")

searchicon2 = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
searchicon2.click()


time.sleep(0.5)

Product2 = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span")
Product2.click()

elemento2 = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[9]/div[6]/div[1]/div[4]/div/div/div/div/div/form/div/div/div/div/div[3]/div/div[13]/div[1]/span/span/span/input")
elemento2.click()

time.sleep(0.5)
carrito = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[3]/div/a[5]")
carrito.click()