# Zum Senden über Google Mail "Zugriff auf weniger sichere Apps" (kurzfristig) einschalten

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Create a text/plain message
msg = EmailMessage()
msg.set_content("""
Hallo liebe Freunde!

Viele Grüße
Michael
""")

msg['Subject'] = "Mein Betreff"
# msg['From'] = "micman1@googlemail.com"
msg['To'] = "mic@mailinator.com"

# Send the message via our own SMTP server.
s = smtplib.SMTP('smtp.gmail.com')       # ('localhost')
username = input("Username?")
msg["From"] = username # + "@googlemail.com"
password = input("Passwort?")
s.starttls()
s.login(username, password)
# username: gabi42
# kenntwort: gabi42-4711

s.send_message(msg)
s.quit()

# Aufgabe: Anhang anhaengen
