# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Create a text/plain message
msg = EmailMessage()
msg.set_content("""
Hallo Freunde!

Viele Grüße,
Michael
""")

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = "Test Mail von Python"
msg['From'] = "micman1@googlemail.com"
msg['To'] = "mic@mailinator.com"

# Send the message via our own SMTP server.
s = smtplib.SMTP('smtp.gmail.com')
s.starttls()
username = input("Username?")
password = input("Password?")
s.login(username, password)

s.send_message(msg)
s.quit()