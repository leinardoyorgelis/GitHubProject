import requests
import json

def send_email(subject, body):
    url = "https://accounts.sandbox.google.com/oath/signup"
    data = {
        'email': 'your-email@example.com',
        'password': 'your-password',
        'subject': subject,
        'body': body
    }
    response = requests.post(url, data=data)
    return response.text

print(send_email("Sample Email", "This is a sample email. It's intended to be sent from the GitHub project for School by me."))
