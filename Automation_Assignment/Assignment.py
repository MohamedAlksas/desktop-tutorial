import ftplib
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='ftp_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

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
    # Replace with your FTP server details
    FTP_SERVER = 'eu-central-1.sftpcloud.io'  # Example of a free FTP server
    USERNAME = '806a333a92344bfe85ead91cc9e08d01'             # Example username
    PASSWORD = 'csJnaZzOpbr1mAXG2lzgcP6vIK43vzOh'  # Example password
    FILE_TO_UPLOAD = 'test.txt'      # Ensure this file exists in the current directory

    connect_and_upload(FTP_SERVER, USERNAME, PASSWORD, FILE_TO_UPLOAD)