# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Creat a text/plain message
msg = EmailMessage()
msg.set_content("""
Hallo liebe Freunde!

Viele Grüße Gabi
""")

msg['Subject'] = "Mein Betreff"
msg['From'] = "gabi@mailinator.com"
msg['To'] = "anna@mailinator.com"

# Send the message via our own SMTP server.
s = smtplib.SMTP('smtp.gmail.com')
username = input("Username?")
password = input("Password?")
s.starttls()
s.login(username, password)
# username
# Kennwort
s.send_message(msg)
s.quit()