# TQ1

The test cases are written in Python and run in Linux environment. In order to run this script, you need to have python 2.7 installed on you linux PC.
Once python is installed and set up, clone this repo to your local pc.

Once cloning is completed, then get into the cloned directory and look for "main.sh" 

main.sh is the shell script, that is used here to invoke indvidual python scripts for given test cases. To run, test cases, selenium and geckodriver must be installed. To install selenium on ubuntu,open Terminal and type below commands :
    $ sudo apt-get install python-pip
    $ sudo pip install selenium
Install geckodriver : Go to https://github.com/mozilla/geckodriver/releases/download/v0.19.0/geckodriver-v0.19.0-linux64.tar.gz and download latest version of geckodriver for ubuntu 64 bit.

Go to downloads folder and extract geckodriver-v0.19.0-linux64.tar.gz to extract binary of geckodriver.
Move geckodriver binary to /usr/local/bin/ by giving command as : sudo mv geckodriver /usr/local/bin/ 
change permissions for geckodriver .
    cd /usr/local/bin
    sudo chmod 777 geckodriver
    
Once selenium and geckodriver are installed then run "main.sh" to completely run selenium test cases.

How to run main.sh ?
In order to run main.sh you have to give command in terminal as below :
    sh main.sh > logs.txt
On pressing Enter, the selenium test cases will start executing and all the logs will get captured in logs.txt that can be analyzed later for failures (if any)

-------------------------------------
Test cases are as per given requirements :

HTTP.py : It basically checks if Site is operational or not.

PublishTests.py : It is used to login user to the admin panel, create a post and verify if posts are available in Index page or not. Also, it verifies if user is able to see "anything" in bold 

Commenttests.py : It covers test cases for adding , viewing and replying to comments made by users of the blog.

  
