import time
from selenium.webdriver.common.by import By
import pyperclip

#login module 
def login_facebook_m(driver, username, password, delay):
    time.sleep(delay)
    username_field = driver.find_element("id","m_login_email")
    username_field.send_keys(username)
    password_field = driver.find_element("id","m_login_password")
    password_field.send_keys(password)
    driver.find_element("id", "login_password_step_element").click()
    time.sleep(delay)
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(delay)

def login_facebook_mobile(driver, username, password, delay):
    time.sleep(delay)
    username_field = driver.find_element("id","m_login_email")
    username_field.send_keys(username)
    password_field = driver.find_element(By.XPATH,"//input[@type='password']")
    password_field.send_keys(password)
    driver.find_element(By.XPATH,"//input[@value='Log In']").click()
    time.sleep(delay)
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(delay)

def join_grp_and_return_name(driver, group_id, delay, username):
    time.sleep(delay)
    group_url = "https://www.facebook.com/groups/" + str(group_id)
    driver.get(group_url)
    time.sleep(delay)
    try:  
        grp_name = driver.find_element(By.XPATH,"//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv x1xlr1w8']").get_attribute('textContent')
        time.sleep(delay)
        try:
            try:
                driver.find_element(By.XPATH,"//span[text()='Join Group']").click()
                time.sleep(delay)
                temp = username + "Join Group "+ group_id
            except:
                driver.find_element(By.XPATH,"//span[text()='Join group']").click()
                time.sleep(delay)
                temp = username + "Join Group "+ group_id
        except:   
            print(grp_name,"Grp already joined")
            username = username.replace("\n","")
            temp = username + " Already joined Group "+ group_id
        return grp_name
    except:
        temp = username + "Group is private "+ group_id
        return temp

def logout(driver, delay):
    driver.find_element(By.XPATH,"//div[@class='x78zum5 x1n2onr6']").click()
    time.sleep(delay)
    driver.find_element(By.XPATH,"//span[text()='Log Out']").click()
    time.sleep(delay)
    driver.get("https://m.facebook.com/")
    time.sleep(delay)
    driver.find_element(By.XPATH,"//div[text()='Log in to another account']").click()
    time.sleep(delay)
    
def professional_dashboard(driver, delay):
    try:
        driver.find_element(By.XPATH,"//div[@class='x1rg5ohu x1n2onr6 x3ajldb x1ja2u2z']").click()
        time.sleep(delay)
        driver.find_element(By.XPATH,"//div[@class='x9f619 x1n2onr6 x1ja2u2z x78zum5 x2lah0s x1qughib x6s0dn4 xozqiw3 x1q0g3np x1sxyh0 xurb0ha xwib8y2 x1y1aw1k xcud41i x139jcc6 x4vbgl9 x1rdy4ex']").click()
        time.sleep(delay)
        driver.find_element(By.XPATH,"//div[@aria-label='See options']").click()
        time.sleep(delay)
        driver.find_element(By.XPATH,"//span[text()='Turn on professional mode']").click()
        time.sleep(delay)
        driver.find_element(By.XPATH,"//span[text()='Turn on']").click()
        time.sleep(delay)
    except:
        try:
            driver.find_element(By.XPATH,"//span[text()='Lock profile']").click()
            time.sleep(delay)
            driver.find_element(By.XPATH,"//span[text()='Lock Your Profile']").click()
            time.sleep(delay)
            driver.find_element(By.XPATH,"//span[text()='Ok']").click()
            time.sleep(delay)
            driver.find_element(By.XPATH,"//div[@class='x1rg5ohu x1n2onr6 x3ajldb x1ja2u2z']").click()
            time.sleep(delay)
            driver.find_element(By.XPATH,"//span[text()='Unlock profile']").click()
            time.sleep(delay)   
            driver.find_element(By.XPATH,"//div[@aria-label='Unlock']").click()
            time.sleep(delay)   
            driver.find_element(By.XPATH,"//span[text()='Unlock Your Profile']").click()
            time.sleep(delay)   
            driver.find_element(By.XPATH,"//span[text()='OK']").click()
            time.sleep(delay)  
            driver.find_element(By.XPATH,"//div[@aria-label='See options']").click()
            time.sleep(delay)
            driver.find_element(By.XPATH,"//span[text()='Turn on professional mode']").click()
            time.sleep(delay)
            driver.find_element(By.XPATH,"//span[text()='Turn on']").click()
            time.sleep(delay)
        except:
            driver.find_element(By.XPATH,"//span[text()='Unlock profile']").click()
            time.sleep(delay)
            driver.find_element(By.XPATH,"//div[@aria-label='Unlock']").click()
            time.sleep(delay)
            driver.find_element(By.XPATH,"//div[@aria-label='Unlock Your Profile']").click()
            time.sleep(delay)
            driver.find_element(By.XPATH,"//div[@aria-label='OK']").click()
            time.sleep(delay)
            driver.find_element(By.XPATH,"//div[@aria-label='See options']").click()
            time.sleep(delay)
            driver.find_element(By.XPATH,"//span[text()='Turn on professional mode']").click()
            time.sleep(delay)
            driver.find_element(By.XPATH,"//span[text()='Turn on']").click()
            time.sleep(delay)
            pass

def create_link(driver, delay, setting):
    try:
        post_list = []
        post_file = open("_post_id.txt", "r")
        for line in post_file:
            post_list.append(line.replace("\n",""))
            
        post_ID = post_list[0]
        driver.get(post_ID)
        time.sleep(delay)
        driver.find_element(By.XPATH,"//span[text()='Share']").click()
        time.sleep(delay)
        driver.find_element(By.XPATH,"//span[text()='Share to a group']").click()
        time.sleep(delay)
        grp_name = setting['new_group_name']
        element_id = "//span[text()='"+ grp_name +"']"
        driver.find_element(By.XPATH,element_id).click()
        time.sleep(delay)
        element = "//i[@style='"+"height: 24px; width: 24px; background-image: url("+'"https://static.xx.fbcdn.net/rsrc.php/v3/yW/r/FUORWl2ZrHy.png'+'"); background-position: 0px -37px; background-size: auto; background-repeat: no-repeat; display: inline-block;'+"']"
        driver.find_element(By.XPATH,element).click()
        time.sleep(delay)
        driver.find_element(By.XPATH,"//span[text()='Feeling/activity']").click()
        time.sleep(delay)
        driver.find_element(By.XPATH,"//input[@aria-label='Feeling']").send_keys("cool")
        time.sleep(delay)
        driver.find_element(By.XPATH,"//div[@class='xamitd3 x1r8uery x1iyjqo2 xs83m0k xeuugli']").click()
        time.sleep(delay)
        driver.find_element(By.XPATH,"//span[text()='Post']").click()
        time.sleep(delay)
    except:
        print("Sharing to group failed")
    try:
        driver.get("https://www.facebook.com/groups/feed/")
        time.sleep(delay)
        grp_name = setting['new_group_name']
        element_id = "//span[text()='"+ grp_name +"']"
        driver.find_element(By.XPATH,element_id).click()
        time.sleep(delay)
        driver.find_element(By.XPATH,"//span[text()='Share']").click()
        time.sleep(delay)
        driver.find_element(By.XPATH,"//span[text()='Copy link']").click()
        time.sleep(delay)
        original_post_link = pyperclip.paste()
        pyperclip.copy(original_post_link)
        print(original_post_link)
        time.sleep(delay)
        print('Done creating and generating link')
        return original_post_link
    except:
        print("Failed to get link")