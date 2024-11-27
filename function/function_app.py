import azure.functions as func
import logging
import os

import requests
from dotenv import load_dotenv
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient

load_dotenv()

# SendGrid environment variables
sender = os.getenv("EMAIL_SENDER")
api_url = os.getenv("API_DOMAIN")
sendgrid_secret = os.getenv("SG_KEY")
secret_key_func = os.getenv("SECRET_KEY_FUNC")

app = func.FunctionApp()

@app.queue_trigger(arg_name="azqueue", queue_name="account-activation",
                               connection="saaccountingsystemdev_STORAGE") 
def QueueTriggerFunctionActivateAccount(azqueue: func.QueueMessage):
    
    # Extract body from queue message
    body = azqueue.get_body().decode('utf-8')

    # Request authorization code from api
    response = requests.post(
        f"{api_url}/user/{body}/auth_code",
        headers={"Authorization": secret_key_func}
    )
    
    response.raise_for_status()                     # Check response status
    auth_code = response.json().get('auth_code')    # Extract auth_code from response
    
    # Compose account activation email with auth_code
    message = Mail(
        from_email=sender,
        to_emails=body,
        subject="Queues Project: Account Activation",
        plain_text_content=f"Your account activation code is: {auth_code}",
        html_content=f"Your account activation code is: <strong>{auth_code}</strong>"
    )
    
    # Send email through sendgrid api
    try:
        sg = SendGridAPIClient(sendgrid_secret)
        response = sg.send(message=message)     # Send email
        logging.info(response.status_code)      # Log response status
    except Exception as e:
        print(e, e.body if hasattr(e, 'body') else "", sep="\n") # Print exception and body if present
        
    # Logs
    logging.info('Python Queue trigger processed a message: %s', body)
