# Let's use the smtplib to send emails
import smtplib
from email.message import EmailMessage

# Lets define the email addresses of the recipients and our account details
recipient_email_accounts = ["email1@email.com", "email2@email.com"]
my_email = "myemail@test.com"
my_password = "put password here"

# We can now specify the content, subject and recipients of the email
email_msg = EmailMessage()
email_msg['subject'] = "The subject of the email"
email_msg['From'] = my_email
email_msg['To'] = recipient_email_accounts
email_msg.set_content("Put the content of the email here")

# Finally we send the mail. In this example using gmail server
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(my_email, my_password)
    smtp.send_message(email_msg)

# Please Like Subscribe and Share