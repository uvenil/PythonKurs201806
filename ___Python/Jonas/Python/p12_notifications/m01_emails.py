# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage


# Create a text/plain message
msg = EmailMessage()
msg.set_content("""
Hallo liebe Anna!

Viele Grüße
Gabi
""")

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Mein Betreff'
msg['From'] = "gabi@mailinator.com"
msg['To'] = "anna@mailinator.com"

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost') #user name mail.gmx.net
                   # passwort in weitere Zeile
s.send_message(msg)
s.quit()
