import smtplib 
from email.message import EmailMessage
from typing import Dict 

email_subject = "Email test from Python" 
sender_email_address = "carlos97brito@hotmail.com" 
receiver_email_address = "receiver_email@address.com" 
email_smtp = "smtp.gmail.com" 
email_password = "250356!Nelson." 


def start_smtp_server() -> smtplib.SMTP:
	# Set smtp server and port 
	server = smtplib.SMTP(email_smtp, 587) 

	# Identify this client to the SMTP server 
	server.ehlo() 

	# Secure the SMTP connection 
	server.starttls() 

	# Login to email account 
	server.login(sender_email_address, email_password) 

	return server


def send_message(server: smtplib.SMTP, data: Dict[str, str]) -> None:

	# Create an email message object 
	message = EmailMessage() 

	# Configure email headers 
	message['Subject'] = data["subject"] 
	message['From'] = sender_email_address
	message['To'] = data["email"] 

	# Set email body text 
	message.set_content(data["content"]) 

	# Send email 
	server.send_message(message) 



# # Close connection to server 
# server.quit()


