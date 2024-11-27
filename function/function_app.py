import azure.functions as func
from dotenv import load_dotenv
import logging
import os

load_dotenv()

app = func.FunctionApp()

@app.queue_trigger(arg_name="azqueue", queue_name="account-activation",
                               connection="saaccountingsystemdev_STORAGE") 
def QueueTriggerFunctionActivateAccount(azqueue: func.QueueMessage):
    body = azqueue.get_body().decode('utf-8')    
    logging.info('Python Queue trigger processed a message: %s', body)
