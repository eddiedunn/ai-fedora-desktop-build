import sys
import base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Update these paths as needed
client_secret_file = '/path/to/client_secret.json'
refresh_token_file = '/path/to/refresh_token'
recipient_email = "recipient@example.com"


def main():
    with open(refresh_token_file, 'r') as f:
        refresh_token = f.read().strip()

    client_id, client_secret = get_client_info(client_secret_file)

    credentials = Credentials.from_authorized_user_info(info={"refresh_token": refresh_token},
                                                         client_id=client_id,
                                                         client_secret=client_secret)

    try:
        send_email(credentials)
    except HttpError as error:
        print(f'An error occurred: {error}')
        sys.exit(1)

def send_email(credentials):
    service = build('gmail', 'v1', credentials=credentials)
    message = create_message("you@example.com", "recipient@example.com", "RAID Alert", "RAID event occurred.")
    send_message(service, "me", message)

def create_message(sender, to, subject, message_text):
    message = {'raw': base64.urlsafe_b64encode((f"From: {sender}\nTo: {to}\nSubject: {subject}\n\n{message_text}").encode('utf-8')).decode('utf-8')}
    return message

def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print(f"Message Id: {message['id']}")
    except HttpError as error:
        print(f'An error occurred: {error}')
        message = None
    return message

def get_client_info(client_secret_file):
    with open(client_secret_file, "r") as f:
        data = json.load(f)
    client_id = data["installed"]["client_id"]
    client_secret = data["installed"]["client_secret"]
    return client_id, client_secret

if __name__ == '__main__':
    main()
