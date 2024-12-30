import random
import smtplib
from email.message import EmailMessage

# Generate a 6-digit OTP
otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])

# SMTP setup
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

from_mail = 'ujwalkatre2004@gmail.com'
app_password = 'ohak ffri qdbk jqeq'  # Replace with a valid app password

try:
    # Login to the email account
    server.login(from_mail, app_password)
    
    # Get recipient's email
    to_mail = input("Enter your email: ")
    
    # Create and send the email
    msg = EmailMessage()
    msg['Subject'] = "OTP Verification"
    msg['From'] = from_mail
    msg['To'] = to_mail
    msg.set_content(f"Your OTP is: {otp}")
    
    server.send_message(msg)
    print("OTP sent successfully. Verify your email.")
    
    # OTP verification
    input_otp = input("Enter your OTP: ")
    if input_otp == otp:
        print("OTP Verified")
    else:
        print("Invalid OTP")

except smtplib.SMTPAuthenticationError:
    print("Failed to authenticate. Check your email and password.")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Ensure the server connection is closed
    server.quit()
