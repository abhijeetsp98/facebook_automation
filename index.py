import time
import utils
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from multiprocessing import Process

# read setting values 
setting_file = open("_settings.txt", "r")
setting = {}
for line in setting_file:
    if line.split('=')[0].replace(' ',"") != 'activity_subject':
        value = line.split('=')[1].replace("\n","").replace(' ',"")
        setting[line.split('=')[0].replace(' ',"")] = value.replace(' ',"")
    else:
        value = line.split('=')[1].replace("\n","")
        setting[line.split('=')[0].replace(' ',"")] = value

# read username and password
user_pass_file = open("_userid_pass.txt", "r")
user_names = []
total_user = 0
for line in user_pass_file:
    user_names.append(line)
    total_user = total_user + 1
total_user = total_user - 1

def main_flow(id, driver, username, password ):
    # action = ActionChains(driver)e
    delay = int(setting['delay'])
    time.sleep(delay*id)
    # # Main Automation
    try:
        try:
            if setting['phone_login'] == 'yes':
                driver.get("https://mbasic.facebook.com/")
                utils.login_facebook_mobile(driver, username, password, delay)
            else:
                driver.get("https://p.facebook.com/")
                utils.login_facebook_m(driver, username, password, delay)
            driver.get("https://facebook.com/")
            time.sleep(delay)
            utils.professional_dashboard(driver, delay)
        except:
            print("User is blocked skipping it")
            driver.get("https://facebook.com/")
            time.sleep(delay)
            #utils.logout(driver, delay)
            pass
        try:
            time.sleep(delay)
            driver.get("https://www.facebook.com/groups/create/")
            time.sleep(delay)
            driver.find_element(By.XPATH,"//input[@class='x1i10hfl xggy1nq x1s07b3s x1kdt53j x1a2a7pz xjbqb8w x76ihet xwmqs3e x112ta8 xxxdfa6 x9f619 xzsf02u x1uxerd5 x1fcty0u x132q4wb x1a8lsjc x1pi30zi x1swvt13 x9desvi xh8yej3 x15h3p50 x10emqs4']").send_keys(setting['new_group_name'])
            time.sleep(delay)
            driver.find_element(By.XPATH,"//label[@aria-label='Choose privacy']").click()
            time.sleep(delay)
            driver.find_element(By.XPATH,"//span[text()='Public']").click()
            time.sleep(delay)
            driver.find_element(By.XPATH,"//span[text()='Create']").click()
            print('Done creating group')
        except Exception:
            print('Failed Creating group and generating link')
            pass
        try:
            time.sleep(delay)
            viral_link = utils.create_link(driver, delay, setting)
            print(viral_link)
        except:
            print("Link creation failed")
        try:
            group_list = []
            group_file = open("_group_id.txt", "r")
            for line in group_file:
                group_list.append(line.replace("\n",""))
            grp_no = len(group_list)

            for i in range(10):
                index = min(i+id*10, grp_no-1)  
                group_name = utils.join_grp_and_return_name(driver, group_list[index], delay, username)
                time.sleep(delay)
                try:
                    driver.get(viral_link)
                    time.sleep(delay)
                    driver.find_element(By.XPATH,"//span[text()='Share']").click()
                    time.sleep(delay)
                    driver.find_element(By.XPATH,"//span[text()='Share to a group']").click()
                    element_share = "//span[text()='" + group_name + "']"
                    time.sleep(delay)
                    driver.find_element(By.XPATH,element_share).click()
                    time.sleep(delay)

                    try:
                        with open('_activity_id.txt', 'r') as file:
                            data = file.read().replace('\n', '')
                        username_field = driver.find_element(By.XPATH,"//div[@aria-label='Create a public post…']")
                        username_field.send_keys(data)
                        time.sleep(delay)
                        driver.find_element(By.XPATH,"//div[@aria-label='Feeling/activity']").click()
                        time.sleep(delay)
                        driver.find_element(By.XPATH,"//div[@aria-selected='false' and @class='x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou xe8uvvx xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x87ps6o x1lku1pv x1a2a7pz xjyslct xjbqb8w x18o3ruo x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1heor9g x1ypdohk xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg x1vjfegm x3nfvp2 xrbpyxo xng8ra x16dsc37'] ").click()
                        time.sleep(delay)
                        driver.find_element(By.XPATH,"//input[@aria-label='Activity']").send_keys(setting['activity'])
                        time.sleep(delay)
                        driver.find_element(By.XPATH,"//span[text()='"+ setting['activity'] +"']").click()
                        time.sleep(delay)
                        driver.find_element(By.XPATH,"//input[@aria-label='Activity']").send_keys(setting['activity_subject'])
                        time.sleep(delay)
                        driver.find_element(By.XPATH,"//span[text()='"+ setting['activity_subject'] +"']").click()
                        time.sleep(delay)
                    except:
                        print("Fail to set activity")
                    driver.find_element(By.XPATH,"//span[text()='Post']").click()
                    time.sleep(delay*2)
                    print("Activity applied successfully")
                except:
                    print("Not able to share the link to grp")
                # with open("my_file.txt", "a") as my_file:
                #     my_file.write(group_name) 
                # print(group_name)
        except:
            print('Failed sharing link execution')
            time.sleep(9999)
            pass

    except Exception as e:      
        print("exception occured")
        print(e)
        pass


num = int(setting['concurrent'])
process = [None] * num

def get(id, Driver):
    if user_names[id] == user_names[len(user_names)-1]:
        return
    option = Options()
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    # option.add_argument("--disable-extensions")
    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option(
        "prefs", {"profile.default_content_setting_values.notifications": 2}
    )
    driver = Driver( chrome_options=option, executable_path="C:\chromedriver.exe")
    print(user_names[id])
    main_flow(id, driver, user_names[id], user_names[len(user_names)-1])
    return

if __name__ == '__main__':
    num = min(num, total_user)
    num = 1
    for i in range(num):
        process[i] = Process(target=get, args = [i, webdriver.Chrome])
        process[i].start()

    for i in range(num):
        process[i].join()