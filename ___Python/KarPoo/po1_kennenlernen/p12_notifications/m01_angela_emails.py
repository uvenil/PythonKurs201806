# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Create a text/plain message
msg = EmailMessage()
msg.set_content("""

# Create a text/plain message
msg = EmailMessage()

msg['Subject'] = "Mein Betreff"
msg['To'] = "micman1@googlemail.com"

# Send the message via our own SMTP server.
s = smtplib.SMTP('smtp.gmail.com')
username = input("Username?")
msg["From"] = username
password = input("Passwort?")
s.starttls()
s.login(username, password)
s.send_message(msg)
s.quit()

""")

msg['Subject'] = "Mein Betreff"
msg['To'] = "micman1@googlemail.com"

# Send the message via our own SMTP server.
s = smtplib.SMTP('smtp.gmail.com')
username = input("Username?")
msg["From"] = username
password = input("Passwort?")
s.starttls()
s.login(username, password)
s.send_message(msg)
s.quit()

# Aufgabe: Anhang anhaengen