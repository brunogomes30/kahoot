import time
from threading import Timer
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

driver1 = webdriver.Chrome("C:\\Users\\ultra\\OneDrive\\Desktop\\chromedriver.exe",chrome_options=chrome_options) #,chrome_options=chrome_options
driver2 = webdriver.Chrome("C:\\Users\\ultra\\OneDrive\\Desktop\\chromedriver.exe",chrome_options=chrome_options) #,chrome_options=chrome_options
driver3 = webdriver.Chrome("C:\\Users\\ultra\\OneDrive\\Desktop\\chromedriver.exe",chrome_options=chrome_options) #,chrome_options=chrome_options
#driver.get("https://ts2.lusobrasileiro.travian.com/")
#login
#driver.find_element_by_name("name").send_keys(username)
#driver.find_element_by_name("password").send_keys(password)
driver1.get("https://kahoot.it/")
driver2.get("https://kahoot.it/")
driver3.get("https://kahoot.it/")   

pin = input("Pin?").strip()
#names = (">","FPRO","MDIS")
names =  ("Notas?","Quando?","Chumbo?")
answers = [0,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,1]
drivers = (driver1,driver2,driver3)
u_index = 0
while(u_index<3):
    try:
        driver = drivers[u_index]
        driver.find_element_by_name("gameId").send_keys(pin)
        driver.find_element_by_css_selector("button").click()
        #time.sleep(3)
        #user_input = driver.find_element_by_id("nickname")
        while(True):
            try:
                user_input = driver.find_element_by_id("nickname")
                break
            except Exception:
                time.sleep(0.2)
                continue
        user_input.send_keys(names[u_index])
        u_index +=1
        driver.find_element_by_css_selector("button").click()
    except Exception:
        time.sleep(0.5)
#for driver in drivers:
#    driver.get("https://kahoot.it/")
#    driver.find_element_by_name("gameId").send_keys(pin)
#    driver.find_element_by_css_selector("button").click()
#    time.sleep(3)
#    driver.find_element_by_id("nickname").send_keys(names[u_index])
#    u_index +=1
#    driver.find_element_by_css_selector("button").click()
        
i = 0
i1=0
i2=0
i3=0
def loop1():
    global i
    while(True):
        try:
            #print(i)
            driver1.find_element_by_css_selector("div > button:nth-child("+str(answers[i]+1)+")").click()
            #time.sleep(0.05)
            driver2.find_element_by_css_selector("div > button:nth-child("+str(answers[i]+1)+")").click()
            #time.sleep(0.05)
            driver3.find_element_by_css_selector("div > button:nth-child("+str(answers[i]+1)+")").click()
            #loop2()
            i+=1
            #loop1()
        except Exception:
            #t = Timer(0.01,loop1)
            #t.start()
            time.sleep(0.01)
        
def loop2():
    global i2
    try:
        driver2.find_element_by_css_selector("div > button:nth-child("+str(answers[i2]+1)+")").click()
        i2+=1
        loop3()
    except Exception:
        pass
        #t = Timer(0.2,loop2)
        #t.start()
        
def loop3():
    global i3
    try:
        driver3.find_element_by_css_selector("div > button:nth-child("+str(answers[i3]+1)+")").click()
        i3+=1
        #loop3()
    except Exception:
        pass
        #t = Timer(0.2,loop3)
        #t.start()
        
        
t1 = Timer(0.05,loop1)
#t2 = Timer(0.05,loop2)
#t3 = Timer(0.05,loop3)
t1.start()
#t2.start()
#t3.start()
