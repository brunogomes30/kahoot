from threading import Timer
from selenium import webdriver
import time
#Selenium will be used so python clicks on websites
import string

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
N = 50
a=list(string.printable)
digits = a
print(digits)

#username = input("Enter the username you want to win in Kahoot")
#number_of_questions = input("Enter how many questions will there be")
pin = 33683
username = "JCL "
#print("loop")
k = 0
def loop():
    global k
    print(k)
    #print("loop")
    driver = webdriver.Chrome("C:\\Users\\ultra\\OneDrive\\Desktop\\chromedriver.exe",options=chrome_options) #options=chrome_options
    driver.get("https://kahoot.it/")

    pin_box = driver.find_element_by_id("game-input")
    pin_box.send_keys(pin)
    pin_box.submit()
    driver.implicitly_wait(6)

    
    

    #driver.implicitly_wait(2)
    name_box = driver.find_element_by_id("nickname")
    name_box.send_keys(usernames.pop())
    k+=1
    name_box.submit()
    #driver.implicitly_wait(30)
    #driver.close()
    

    
usernames = []
for i in range(0,N):
    print(i)
    user = username + str(digits[i])
    
    usernames.append(user)
    print(usernames)
    t = Timer(0.1,loop)
    t.start()
    time.sleep(0.5)
input()