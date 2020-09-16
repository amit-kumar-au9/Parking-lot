import smtplib

gmail_user = 'anonymous.people.one@gmail.com'
gmail_password = 'slxfyyaaemsukkdv'

sent_from = gmail_user
to = ['amitkumar.developer1@gmail.com']
subject = 'OMG Super Important Message'
body = 'Testing mail'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()
    print('Email sent!')
except Exception:
    print('Something went wrong...')
