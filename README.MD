#About
This script grabs the tweets from the people you follow on the twitter and mail the tweets to the mailid you provide .
The purpose of the script is to get the tweets of only people you need.I have developed this script just to gratify my hungry of exploring :)
#Description
- I have used **tweepy API** ,**smtplib** in the script .
- The file _stream.py_ streams through the twitter and grabs the tweets .
- The file _email_s.py_ mails the tweets to the gmailid you provide in the script.
#Instructions to Run the script
- In order to run the script first get the local Repo of this.
- Create virtual environment and install the packages: 
    - tweepy
    - smtplib
# Things to know:
- This script works only with g-mail accounts.
- Before using the g-mail make sure you change the settings in the _manage account_ section to allow acces to third party apps.
- In order to use the script you need to have twitter [developer account](https://developer.twitter.com/en) ,because the script needs 
access_token ,access_token_secret ,consumer_key ,consumer_key_secret.
- In order to input  the above credentials you need to set the evrionment variable in the system ,if it doesn't work 
set variables through command line .check file _stream.py_ for info.
- In the _stream\_s.py_ file you need to manually enter the twitter id of the people you need tweets to be mailed.
- In the _email\_s.py_ file you need to provide the mailid and passwords, for more info check the file. 
- After everything is done run only the _email\_s.py_.




    
