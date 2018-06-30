# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Create a text/plain message
msg = EmailMessage()
msg.set_content("""
Hallo liebe Freunde!

Viele Grüße
Carsten
""")

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Mein Betreff'
msg['From'] = user
msg['To'] = user

# Send the message via our own SMTP server.
s = smtplib.SMTP('mail.gmx.net')

s.send_message(msg)
s.quit()
