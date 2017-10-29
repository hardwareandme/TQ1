#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
try:
    browser.get("http://ec2-54-90-154-147.compute-1.amazonaws.com/wp-login.php")
    #Check if login page has loaded successfully
    assert "Log In" in browser.title
    print "Login page loaded\n"
    time.sleep(5)
except:
    print "Login page didn't load successfully\n"
    raise Exception(browser.quit())
'''
Find username and Password Tab
Input username and password
'''
try:
    usertab = browser.find_element_by_name("log")
    usertab.clear()
    usertab.send_keys("test_user")
    passtab = browser.find_element_by_name("pwd")
    passtab.clear()
    passtab.send_keys("testuser@123")
    login_button = browser.find_element_by_name("wp-submit")
    login_button.click()
    assert "Dashboard" in browser.title
    print "User logged in successfully\n"
    time.sleep(5)
except:
    print "User login failed\n"
    raise Exception(browser.quit())
'''
Create a New Post by logged in User
'''
try:

    print "creating a new post\n"
    NewPost = browser.find_element_by_xpath(".//*[@id='wp-admin-bar-new-content']/a/span[2]")
    NewPost.click()
    '''
    Check if Blog creation page is loaded or not
    '''
    assert "Add New Post" in browser.title
    print "Add post page loaded successfully\n"
    time.sleep(5)
except:
    print "Add post page didn't load\n"
    raise Exception(browser.quit())
'''
Start adding content
'''
try:
    PostTitle = browser.find_element_by_xpath(".//*[@id='title']")
    PostTitle.send_keys("This is a blog by a test_user")
    PostContent = browser.find_element_by_xpath(".//*[@id='content']")
    PostContent.send_keys("Test user likes to blog. The content of the blog can be <b>anything</b>.")
    time.sleep(5)
    '''
    Publish Post
    '''
    PublishButton = browser.find_element_by_name("publish")
    if PublishButton.is_enabled():
        PublishButton.click()
    assert "Edit Post" in browser.title
    print "post published successfully\n"
    time.sleep(5)
except:
    print "Something went wrong while publishing post\n"
    raise Exception(browser.quit())
# browser.quit()
'''
Check if unauthenticated user is able to see the post 
'''
try:
    browser.get('http://ec2-54-90-154-147.compute-1.amazonaws.com/')
    #check if post is available on Home Page or not
    PostAvailable = browser.find_element_by_link_text("This is a blog by a test_user")
    PostAvailable.click()
    assert "CAN'T BE FOUND." not in browser.page_source
    print "Unauthenticated user is able to see published post"
except:
    print "User is not able to see published post\n"
    raise Exception(browser.quit())

'''
check if user is able to see 'anything' in Bold
'''
try:
    '''
    Check HTML source to check if user is able to see 'anything' in Bold
    '''

    assert "<b>anything</b>" in browser.page_source
    print "Unauthenticated user is able to see 'anything' in Bold"
except:
    print "user is not able to see 'anything' in bold"
    raise Exception(browser.quit())
browser.quit()
#Close browser session
