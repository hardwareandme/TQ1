echo "Loading testcase1 to check if site is operational"
python HTTP.py
echo "Simply waiting before executing next test case"
sleep 5
echo "Loading testcase 2 to create and verify posts by signed user"
python PublishTests.py
echo "waiting .............."
sleep 5
echo "Loading testcase 3 to check if user is able to comment and reply on posts"
python Commenttests.py

