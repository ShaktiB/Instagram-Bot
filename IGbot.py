from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from time import sleep

class IGbot:
    
    def __init__(self):
        
        #self.driver = webdriver.Chrome(ChromeDriverManager().install()) # Initialize the webdriver
        self.driver = webdriver.Chrome(r'C:\Users\Shakti\.wdm\drivers\chromedriver\80.0.3987.16\win32\chromedriver') # Initialize the webdriver >> UPDATE FOR FINAL VERSION
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.url = self.driver.current_url # Store the current url of the page
        self.usr = '' # The username 
        self.main_url = '' # Main account (feed) page url
        self.profile_url = '' # Profile page url 
        
    def login(self, user, pw): # Log-in to the IG account
        
        self.usr = user # Store the uername for later use if needed
        
        try:
            element_user = WebDriverWait(self.driver,3).until(
                    EC.presence_of_element_located((By.NAME, "username"))) # Wait until the page loads all 'username' element
            
            element_pass = WebDriverWait(self.driver,3).until(
                    EC.presence_of_element_located((By.NAME, "password"))) # Wait until the page loads all 'password' element
            
        
            element_user.send_keys(user) # Enter the username
            element_pass.send_keys(pw) # Enter the password
            element_pass.submit() # Same as pressing the 'Enter' button on the keyboard
            
            # After logging in, a 'Turn on Notifications' pop-up might come up, this handles the pop-up
            # and automatically clicks on "Not Now")
            loaded = None
            count = 0
            while not loaded:
                
                try:
                    
                    loaded = WebDriverWait(self.driver,5).until(
                            EC.presence_of_element_located((By.XPATH, '//button[text()="Not Now"]')))
                    
                    if(loaded):
                        self.driver.find_element_by_xpath('//button[text()="Not Now"]').click()
                        self.url = self.driver.current_url # Store the current url of the page
                        
                except (NoSuchElementException,TimeoutException) as e: 
                    
                    print("'Turn on Notifications' pop-up did not come up or waiting to be loaded")
                    count += 1
                
                if(count>3):
                    break
            
        except NoSuchElementException: 
            
            print("The username and password fields are taking too long to load")
    
    def profile_page(self): # Go to the profile page of the IG account
        
        try:
            btn = WebDriverWait(self.driver,5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,"[aria-label=Profile]")))
            
            if(btn):
                
                btn.click()
    
                self.url = self.driver.current_url # Store the current url of the page     
                
                if(not self.profile_url):
                    self.profile_url = self.driver.current_url
                    
        except (NoSuchElementException,TimeoutException) as e: 
            
            print("Issue with clicking profile button")
            
    def main_page(self): # Go to the main page of the IG account
        
        try:
           
            if (self.url == self.profile_url):
                
#                btn = btn = WebDriverWait(self.driver,5).until(
#                        EC.presence_of_element_located((By.CLASS_NAME,"s4Iyt")))
                
                WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME,"s4Iyt"))).click()
               
                self.url = self.get_url() # Store the current url of the page     
                
                if(not self.main_url):
                    self.main_url = self.driver.current_url
                
                self.get_url() # Get the current url of the page
                
            else:
            
                btn = WebDriverWait(self.driver,5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,"[aria-label=Instagram]")))
            
                if(btn):
    #                wait.until(EC.element_to_be_clickable(By.CLASS_NAME,"s4Iyt")).click()
                    btn.click()
                    
                    self.url = self.driver.current_url # Store the current url of the page     
                    
                    if(not self.main_url):
                        self.main_url = self.driver.current_url
                    
                    self.get_url() # Get the current url of the page
        
        except (NoSuchElementException,TimeoutException) as e: 
            print("Issue with clicking main page button")
    
    def profile_summary(self): # Gives the umber of posts, followers, and follows from the profile page
        
        try:
            psts = WebDriverWait(self.driver,5).until( # Find the 'posts' element on the webpage
                    EC.presence_of_element_located((By.CSS_SELECTOR,"span.g47SY")))      
            posts = int(psts.text) # Get the # of posts
            
            
            flwrs = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span")
            followers = int(flwrs.text)
            
            
            flwng = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span")
            following = int(flwng.text)

            return [posts,followers,following]
        
        except (NoSuchElementException,TimeoutException) as e: 
            print("Issue with getting posts, followers, and following numbers")
        
    def get_url(self): # Get the url of the current page
        
        self.url = self.driver.current_url
        

    def close_driver(self): # Close the webdriver 
        self.driver.close()

def credentials():
    u = input("Enter username:")
    p = input("Enter password:")
    
    return[u,p]


if __name__ == "__main__":
    
    #creds = credentials()
    
    bot = IGbot() # Initialize the IG bot & open IG website
    
    bot.login('shaktii_b','messi914') # Log-in to your account
    
    print(f'The current url is: {bot.url}')
    
    bot.profile_page() # Go to the profile page
    
    print(f'The current url is: {bot.url}')
    
    summary = bot.profile_summary() # The number of posts, followers, and following of the IG account
    print(f"\nPosts: {summary[0]}\nFollowers: {summary[1]}\nFollowing: {summary[2]} \n") # Prin account summary
    print("Followers Ratio: {:.2f}".format(summary[1]/summary[2])) # Print follower ratio 
    
    bot.main_page()
    print(f'The current url is: {bot.url}')
    #sleep(5)
    #bot.close_driver()
    

    
    
    
        




#print(driver.title)
#print(driver.current_url)


