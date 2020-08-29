import sendgrid
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('SENDGRID_APIKEY')

def send(recipient='', sent_from='NO-REPLY@pymailo.com', subject='Default Notification', body='This is a testing or in-completed stuff', debug=False):
    tos = []
    for email in recipient.split(';'):
        tos.append({'email': email})
    if debug: print(f'Sending to: {str(tos)}')

    sg = sendgrid.SendGridAPIClient(api_key=API_KEY)
    data = {
        'personalizations': [
            {
                'to': tos,
                'subject': subject
            }
        ],
        'from': {
            'email': sent_from
        },
        'content': [
            {
                'type': 'text/html',
                'value': f'<p>{body}</p>'
            }
        ]
    }
    if debug: print(f'Sending with data: {str(data)}')

    response = sg.client.mail.send.post(request_body=data)
    if debug: print(f'Sent with response code: {response.status_code}')
    if debug: print(f'Sent with response body: {response.body}')
    if debug: print(f'Sent with response header: {response.headers}')