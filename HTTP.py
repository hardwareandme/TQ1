#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

'''
Invoke firefox and load url under test; 
in this case, url = http://ec2-54-90-154-147.compute-1.amazonaws.com/

'''
try:

    browser = webdriver.Firefox()
    browser.get('http://ec2-54-90-154-147.compute-1.amazonaws.com/')
    '''
    Assert Blog title to confirm, page has loaded successfully
    '''
    assert "user's Blog!" in browser.title
    print "Blog Home Page loaded successfully \n"
    time.sleep(5)
except:
    #Quit browser if an exception occurs
    print "Home Page didn't load\n"
    raise Exception(browser.quit())
browser.quit()
