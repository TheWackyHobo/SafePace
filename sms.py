import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(message, recipient_email, sender_email, sender_password):
    # Set up the SMTP server (using Gmail's SMTP server as an example)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # Gmail uses port 587 with TLS

    # Set up the MIME (Multipurpose Internet Mail Extensions)
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Test Email"  # You can specify your subject here
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port, timeout=10)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

        # Close the connection
        server.quit()

        print(f"Email sent to {recipient_email} successfully!")
    
    except smtplib.SMTPException as e:
        print(f"SMTP Error: {e}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

# Example usage
'''
recipient_email = "keegan.pham@slu.edu"  # Replace with the recipient's email address
message = "SafePace test"
sender_email = "safe.pac3@gmail.com"  # Replace with your Gmail address
sender_password = "vpqo hufr cetl bord"  # Replace with your Gmail app password (if 2FA enabled)
send_email(message, recipient_email, sender_email, sender_password)

gmail sign in info
safe.pac3@gmail.com
$afePac32025
vpqo hufr cetl bord
'''
