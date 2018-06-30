# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Open the plain text file whose name is in textfile for reading.

# Create a text/plain message
msg = EmailMessage()
msg.set_content("""
Liebe Angela, liebe Teilnehmer
    
vielen Dank für die konstruktive Zusammenarbeit
    
""")

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Test'
msg['From'] = 'kar.poo.hou@googlemail.com'
msg['To'] = 'wa0158@hotmail.com'

# Send the message via our own SMTP server.
s = smtplib.SMTP('smtp:gmail.com')
s.starttls()
s.send_message(msg)
s.quit()