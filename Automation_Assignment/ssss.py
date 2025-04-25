import ftplib
import logging
import psutil
import smtplib
from email.message import EmailMessage

logging.basicConfig(filename="performance.log", level=logging.ERROR)


def send_email(sender_email, receiver_email, subject, body, smtp_server, port, password, attachment_path=None):
    # Create an email message
    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.set_content(body)  # Set the email body

    # Attach the error log file if provided
    if attachment_path:
        with open(attachment_path, 'rb') as attachment:
            message.add_attachment(attachment.read(), maintype='text', subtype='plain', filename=attachment_path)

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender_email, password)  # Log in to the email account
            server.send_message(message)  # Send the email
            print("Email sent successfully.")

    except Exception as e:
        print(f"An error occurred while sending the email: {e}")

def ftp_operations(ftp_server, username, password, file_to_upload):
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


def check_system_usage(threshold=75):
    # Get CPU and RAM usage
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent

    # the output message
    output = f"CPU Usage: {cpu_usage}%\nRAM Usage: {ram_usage}%\n"

    # Check if usage exceeds the threshold
    if cpu_usage > threshold or ram_usage > threshold:
        output += "Warning: Resource usage exceeds the threshold!\n"
    else:
        output += "Resource usage is within acceptable limits.\n"

    return output





if __name__ == "__main__":
    # Email configuration
    SENDER_EMAIL = "adelm8267@gmail.com"
    RECEIVER_EMAIL = "mohamedalksas12@gmail.com"
    SUBJECT = "System Resource Usage Report"

    # SMTP server configuration
    SMTP_SERVER = "smtp.gmail.com"
    PORT = 587
    PASSWORD1 = "tvgt hyip azxq sbdz"


    # FTP server configuration
    FTP_SERVER = 'ftp.drivehq.com'
    USERNAME = 'mohamedalksas8267'
    PASSWORD2 = '0192837465'
    FILE_TO_UPLOAD = 'test.txt'

    # Connect to FTP and upload the file
    ftp_operations(FTP_SERVER, USERNAME, PASSWORD2, FILE_TO_UPLOAD)

    usage_report = check_system_usage(threshold=75)

    # Send the email with the system usage report
    send_email(SENDER_EMAIL, RECEIVER_EMAIL, SUBJECT, usage_report, SMTP_SERVER, PORT, PASSWORD1)

    # Send the email with the FTP Report
    send_email(SENDER_EMAIL, RECEIVER_EMAIL, SUBJECT,"There was an error while FTP operations and this is the report", SMTP_SERVER, PORT, PASSWORD1,'ftp_errors.log')





