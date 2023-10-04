import smtplib
import time
from email.mime.text import MIMEText

# Define your email server settings
SMTP_SERVER = "your_smtp_server.com"
SMTP_PORT = 587
SMTP_USERNAME = "your_username"
SMTP_PASSWORD = "your_password"

# Define the email subject and content for rejection
EMAIL_SUBJECT = "Application Update"
EMAIL_CONTENT = ("Dear Candidate,\n\nThank you for your interest in our company and for applying for the position. "
                 "After careful consideration, we regret to inform you that we have selected another candidate for "
                 "this role. We appreciate your time and effort and wish you success in your job "
                 "search.\n\nSincerely,\nThe Hiring Team")

# List of candidates and their last interaction timestamp (in seconds)
candidates = {
    "candidate1@example.com": time.time() - 6 * 24 * 60 * 60,  # 6 days ago
    "candidate2@example.com": time.time() - 4 * 24 * 60 * 60,  # 4 days ago
    "candidate3@example.com": time.time() - 7 * 24 * 60 * 60,  # 7 days ago
}


# Function to send a rejection email
def send_rejection_email(email):
    msg = MIMEText(EMAIL_CONTENT)
    msg["Subject"] = EMAIL_SUBJECT
    msg["From"] = "your_email@example.com"
    msg["To"] = email

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail("your_email@example.com", email, msg.as_string())
        server.quit()
        print(f"Rejection email sent to {email}")
    except Exception as e:
        print(f"Failed to send email to {email}: {str(e)}")


# Iterate through candidates and send rejection emails if inactive for 5 days
for email, last_interaction_timestamp in candidates.items():
    if time.time() - last_interaction_timestamp >= 5 * 24 * 60 * 60:
        send_rejection_email(email)
