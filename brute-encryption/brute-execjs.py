#coding:utf-8
#from selenium import webdriver
import execjs


def mzDes(s,para):
    despara = execjs.get('phantomjs').compile(s).call("strEnc",para,"csc","mz","2017")
    return despara

with open('des.js','r') as mzCrypto:
    
    s = mzCrypto.read()
    with open('users.txt','r') as users:   #des username
        with open('des_users.txt','w') as f4DesUser:
            user = users.readlines()
            for u in user:
                uname = u.strip()
                print uname
                desUsername = mzDes(s,uname)
                print desUsername
                f4DesUser.write(desUsername+'\n')
    
    

    with open('pwdTop54.txt','r') as pwds:   #des password
        with open('des_pwds.txt','w') as f4DesPwd:
            pwd = pwds.readlines()
            for p in pwd:
                passwd = p.strip()
                print passwd
                desPassword = mzDes(s,passwd)
                print desPassword
                f4DesPwd.write(desPassword+'\n')