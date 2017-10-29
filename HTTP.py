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
# '''
# Login user using below details :
# url : http://ec2-54-90-154-147.compute-1.amazonaws.com/wp-login.php
# username : test_user
# password : testuser@123
# '''
# '''
# try:
#     browser.get("http://ec2-54-90-154-147.compute-1.amazonaws.com/wp-login.php")
#     #Check if login page has loaded successfully
#     assert "Log In" in browser.title
#     print "Login page loaded\n"
# except:
#     print "Login page didn't load successfully\n"
#     raise Exception(browser.quit())
# '''
# Find username and Password Tab
# Input username and password
# '''
# try:
#     usertab = browser.find_element_by_name("log")
#     usertab.clear()
#     usertab.send_keys("test_user")
#     passtab = browser.find_element_by_name("pwd")
#     passtab.clear()
#     passtab.send_keys("testuser@123")
#     login_button = browser.find_element_by_name("wp-submit")
#     login_button.click()
#     assert "Dashboard" in browser.title
#     print "User logged in successfully\n"
# except:
#     print "User login failed\n"
#     raise Exception(browser.quit())
# '''
# Create a New Post by logged in User
# '''
# try:
#
#     print "creating a new post\n"
#     NewPost = browser.find_element_by_xpath(".//*[@id='wp-admin-bar-new-content']/a/span[2]")
#     NewPost.click()
#     '''
#     Check if Blog creation page is loaded or not
#     '''
#     assert "Add New Post" in browser.title
#     print "Add post page loaded successfully\n"
# except:
#     print "Add post page didn't load\n"
#     raise Exception(browser.quit())
# '''
# Start adding content
# '''
# try:
#     PostTitle = browser.find_element_by_xpath(".//*[@id='title']")
#     PostTitle.send_keys("This is a blog by a test_user")
#     PostContent = browser.find_element_by_xpath(".//*[@id='content']")
#     PostContent.send_keys("Test user likes to blog. The content of the blog can be <b>anything</b>.")
#     '''
#     Publish Post
#     '''
#     PublishButton = browser.find_element_by_name("publish")
#     PublishButton.click()
#     assert "Edit Post" in browser.title
#     print "post published successfully\n"
# except:
#     print "Something went wrong while publishing post\n"
#     raise Exception(browser.quit())
# #browser.quit()
# '''
# Check Blog post by unauthenticated users
# BrowserForUser = webdriver.Firefox()
# try:
#     '''
#     Open a separate session for testing unauthenticated users
#     '''
#     BrowserForUser.get("http://ec2-54-90-154-147.compute-1.amazonaws.com/")
#     assert "This is a blog by a test_user" in BrowserForUser.page_source
#     print "Unauthenticated user is able to see the post\n"
#     BrowserForUser.quit()
# except:
#     print "User is unable to find post\n"
#     raise Exception(BrowserForUser.quit())
#
# try:
#     '''
#     Navigate logged in user to Home page
#     '''
#     browser.find_element_by_xpath(".//*[@id='wp-admin-bar-site-name']/a").click()
#     '''
#     Load post that user will click
#     '''
#     browser.find_element_by_xpath(".//*[@id='post-2361']/header/h3/a").click()
#     assert "<b>anything</b>" in browser.page_source
#     print "User is able to see 'anything' in Bold\n"
# except:
#     print "'anything' is not visible in Bold\n"
#     raise Exception(browser.quit())
#
#
# #browser.quit()
