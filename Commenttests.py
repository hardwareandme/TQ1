#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()

'''
Create a comment on the Post
'''
try:
    browser.get("http://ec2-54-90-154-147.compute-1.amazonaws.com/")
    # scroll = browser.find_element_by_xpath(".//*[@id='masthead']/div/div[2]/div/a/svg")
    scroll = browser.find_element_by_css_selector(".menu-scroll-down")
    scroll.click()

    postSearch = browser.find_element_by_class_name("search-field")
    postSearch.clear()
    postSearch.send_keys("This is a blog by a test_user")
    postSearch.submit()
    assert "nothing found" not in browser.page_source
    print "post found\n"
    browser.find_element_by_link_text("This is a blog by a test_user").click()
except:
    print "Post not found"
    raise Exception(browser.quit())
'''
Add Comment
'''
try:
    time.sleep(5)
    #find comment field
    comment_section = browser.find_element_by_xpath(".//*[@id='comment']")
    comment_section.clear()
    #add comment
    comment_section.send_keys("Comment by user 1bcd")
    #find email field
    email = browser.find_element_by_xpath(".//*[@id='email']")
    #add email
    email.send_keys("user1@typeset.io")
    #find name field
    Name = browser.find_element_by_xpath(".//*[@id='author']")
    #Add name
    Name.send_keys("User 1")
    submit = browser.find_element_by_xpath(".//*[@id='submit']")
    submit.click()
    time.sleep(30)
    #Check if Duplicate comments exist
    assert "Duplicate comment detected" not in browser.page_source
    print "comment added"
except:
    print "Unable to add comments"
    #raise Exception(browser.quit())
'''
reply comment to comment by user 1
'''
try:
    #find reply button
    replyButton = browser.find_element_by_class_name("comment-reply-link")
    replyButton.click()
    #find comment section
    comment = browser.find_element_by_id("comment")
    comment.clear()
    #add comment
    comment.send_keys("Comment by user2namenb")
    user2name = browser.find_element_by_name("author")
    #clear username field
    user2name.clear()
    #add username
    user2name.send_keys("User 2")
    user2email = browser.find_element_by_name("email")
    #clear email field
    user2email.clear()
    #add email
    user2email.send_keys("user2@typeset.io")
    submit_comment = browser.find_element_by_class_name("submit")
    submit_comment.click()
    time.sleep(10)
    assert "User 2" in browser.page_source
    print "comment 2 is added as a reply to comment 1"
    time.sleep(5)
except:
    print "Reply to comment1 not added"
    raise Exception(browser.quit())
browser.quit()
