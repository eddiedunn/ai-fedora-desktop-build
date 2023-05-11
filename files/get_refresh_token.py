import os
import sys
from google_auth_oauthlib.flow import InstalledAppFlow

client_secret_file = sys.argv[1]
token_file = sys.argv[2]

# Scopes needed for sending an email
scopes = ['https://www.googleapis.com/auth/gmail.send']

flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, scopes)
credentials = flow.run_local_server(prompt='consent', open_browser=True)
refresh_token = credentials.refresh_token

with open(token_file, 'w') as f:
    f.write(refresh_token)

print('Refresh token saved to:', token_file)