import smtplib
from email.mime.text import MIMEText # MIMEText is a class that represents the textg of the email
from email.mime.multipart import MIMEMultipart
import os


def send_email(work_flowname, repo_name,workflow_run_id):
    sender_email  = os.getenv('SENDER_EMAIL')
    sender_password  = os.getenv('SENDER_PASSWORD')
    receiver_email = os.getenv('RECEIVER_EMAIL')


    subject = f"Workflow{work_flowname} failed for repo {repo_name}"
    body = f"Hi  workflow{work_flowname} failed for the repo {repo_name}. please check  the logs for more details.\nMore Details: \nRun_ID: {workflow_run_id}"  
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] =  receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender_email,sender_password)
        server.quit()

        print('Email Sent Successfully')
    except Exception as e :
        print(f'Error: {e}')


send_email(os.getenv('WORKFLOW_NAME'),os.get('REPO_NAME'),os.getenv('WORKFLOW_RUN_ID'))
