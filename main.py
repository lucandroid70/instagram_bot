from selenium import webdriver
from time import sleep
from account import username,password

class InstaBot:
    def __init__(self,username,password): 
        self.username = username
        self.driver = webdriver.Chrome("./chromedriver/chromedriver.exe")
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Inicia sesión')]")\
            .click()   
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)            
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(password)            
        self.driver.find_element_by_xpath("//button[@type='submit']")\
            .click()            
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Ahora no')]")\
            .click()      
        

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")\
            .click()
        sleep(1)        
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        print(names)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div/button/span")\
            .click()
        sleep(1)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Salir')]")\
            .click()           
        self.driver.close()


my_bot = InstaBot(username,password)
my_bot.get_unfollowers()

