import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up your email details
email_from = "asdf@outlook.fr"
email_to = "asdf3@gmail.com"
email_subject = "Hello World"
email_body = "Hello, World!"

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = email_from
message["To"] = email_to
message["Subject"] = email_subject

# Add body to email
message.attach(MIMEText(email_body, "plain"))

# Log in to Gmail's SMTP server
smtp_server = "smtp-mail.outlook.com"
smtp_port = 587
smtp_username = "asdf@outlook.fr"
smtp_password = "asdf"

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_username, smtp_password)

# Send email
text = message.as_string()
server.sendmail(email_from, email_to, text)

# Close the SMTP server
server.quit()

print("Email sent!")
