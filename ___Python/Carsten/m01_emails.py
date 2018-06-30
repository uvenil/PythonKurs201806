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

msg['Subject'] = "Mein Betreff"
msg['To'] = "starke.carsten@gmx.de"

# Send the message via our own SMTP server.
s = smtplib.SMTP('mail.gmx.net')
username = input("Username?")
msg['From'] = username # bei GMX korrespondieren Username und E-Mail-Adresse
password = input("Password?")
s.starttls()
s.login(username, password)
s.send_message(msg)
s.quit()
