"""import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "labratcloud@gmail.com"
receiver_email = "bijin721@gmail.com"
password = input("Type your password and press enter:")
message = """"""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)"""
import smtplib
from email.mime.text import MIMEText
def send_email(a):
  sender_email = "labratcloud@gmail.com"
  sender_password = "sisnuesvoosxaios"
  recipient_email = "bijin721@gmail.com"
  subject = "Price reached discount"
  body = f"""
  <html>
    <body>
      <p> {a} has reached discounted price /p>
    </body>
  </html>
  """
  html_message = MIMEText(body, 'html')
  html_message['Subject'] = subject
  html_message['From'] = sender_email
  html_message['To'] = recipient_email

  server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  server.login(sender_email, sender_password)
  server.sendmail(sender_email, recipient_email, html_message.as_string())
  server.quit()