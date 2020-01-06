from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self,username,password):
        
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)       #it pauses the page for loading purpose for 3 seconds
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(2)
    
    def like_tweet(self,hashtags):
        bot=self.bot
        bot.get('https://twitter.com/search?q=' + hashtags + '&src=typed_query') 
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweetLinks = [i.get_attribute('href')
                for i in bot.find_elements_by_xpath("//a[@dir='auto']")]
            filteredLinks = list(filter(lambda x: 'status' in x,tweetLinks)) 

            for filteredLinks in filteredLinks :
                    bot.get(filteredLinks)
                    time.sleep(5)
                    try:
                        bot.find_element_by_xpath("//div[@data-testid='like']").click()
                        time.sleep(10)
                    except Exception as ex :
                        time.sleep(10)


email_input=input("please enter the email")
password_input=input("please enter the password")
hashtag_input=input("please enter the hashtag")

ap = TwitterBot(email_input,password_input)
ap.login()
ap.like_tweet(hashtag_input)