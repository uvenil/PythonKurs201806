# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Open the plain text file whose name is in textfile for reading.
msg = EmailMessage()
msg.set_content("""textanfang

textende
""")

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Betreff'
msg['From'] = 'gabi@mailinator.com'
msg['To'] = 'anna@mailinator.com'

# Send the message via our own SMTP server.
s = smtplib.SMTP('mail.gmx.de')
s.starttls()
username = input("Username? ")
password = input("password? ")
s.login(username, password)

s.send_message(msg)
s.quit()