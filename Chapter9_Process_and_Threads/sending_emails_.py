import asyncio
import smtplib

async def send_email(subject, body,to):
    content = 'hello world'
    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    sender = 'yourMail@gmail.com'
    recipient='test@gmail.com'
    mail.login('yourMail@gmail.com','***YourPasword****')
    header='To:'+recipient+'\n'+'From:' \
    +sender+'\n'+'subject:testmail\n'
    content=header+content
    mail.sendmail(sender,recipient,content)
    mail.close

async def main():
    asyncio.create_task(send_email('Test Email', 'tihs is a test email', 'you@example.com'))

    # continue with other work wothout for the email to send 
    print('doing other task')

asyncio.run(main())