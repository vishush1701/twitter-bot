import smtplib
from email.message import EmailMessage
import stream_s

email = EmailMessage()
email['from'] = '<from mail id >'
email['to'] = '<to mail id'
email['subject'] = f"Timeline tweets from{stream_s.following}"

stream_s.get_tweets()

with open('tweet.txt', mode='r', encoding='utf-8') as f_p:
    email.set_content(f_p.read())

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('<from mail id >', '<from mail id password>')
    smtp.send_message(email)
    print('mail sent successfully')
    smtp.quit()
