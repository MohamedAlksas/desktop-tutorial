import ftplib
import logging
import smtplib
from email.message import EmailMessage
import ssl
from datetime import datetime

# Configure logging
logging.basicConfig(filename='ftp_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def send_secure_email(sender_email, receiver_email, subject, body, smtp_server, port, password):
    # Create an email message
    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.set_content(body)  # Set the email body

    # Create a secure SSL context
    context = ssl.create_default_context()

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)  # Secure the connection
            server.login(sender_email, password)  # Log in to the email account
            server.send_message(message)  # Send the email
            print("Email sent successfully.")

    except Exception as e:
        print(f"An error occurred while sending the email: {e}")


def connect_and_upload(ftp_server, username, password, file_to_upload):
    try:
        # Connect to the FTP server
        ftp = ftplib.FTP(ftp_server)
        ftp.login(user=username, passwd=password)
        print(f"Connected to {ftp_server}")

        # List files in the current directory
        files = ftp.nlst()
        print("Files on the server:")
        for file in files:
            print(file)

        # Upload the file
        with open(file_to_upload, 'rb') as file:
            ftp.storbinary(f'STOR {file_to_upload}', file)
            print(f"Uploaded {file_to_upload} successfully.")

    except ftplib.all_errors as e:
        logging.error(f"FTP error: {e}")
        print(f"An error occurred: {e}")

    finally:
        try:
            ftp.quit()
            print("Disconnected from the server.")
        except Exception as e:
            logging.error(f"Error disconnecting: {e}")


if __name__ == "__main__":
    # Email configuration
    SENDER_EMAIL = "your_email@example.com"  # Replace with your email
    RECEIVER_EMAIL = "recipient@example.com"  # Replace with recipient's email
    SUBJECT = "FTP Errors Report"

    # Read the contents of the error log file
    error_log_contents = ""
    if logging.getLogger().hasHandlers():
        with open('ftp_errors.log', 'r') as log_file:
            error_log_contents = log_file.read()

    # FTP server configuration
    FTP_SERVER = 'ftp.dlptest.com'  # Example of a free FTP server
    USERNAME = 'dlpuser'  # Example username
    PASSWORD = 'rNrKYTX9g7z3RgJRmxWuGHbeu'  # Example password
    FILE_TO_UPLOAD = 'test.txt'  # Ensure this file exists in the current directory

    # Connect to FTP and upload the file
    connect_and_upload(FTP_SERVER, USERNAME, PASSWORD, FILE_TO_UPLOAD)

    # If there are errors, send an email
    if error_log_contents:
        send_secure_email(SENDER_EMAIL, RECEIVER_EMAIL, SUBJECT, error_log_contents,
                          "smtp.gmail.com", 587, "your_email_password")  # Replace with your email password