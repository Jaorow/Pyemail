import smtplib
import ssl
from email.message import EmailMessage



def send_email(data, email_receiver,password,email_sender = None) -> None:
    """sends email to reciver including data
    
    Keyword arguments:
    data -- a string of data can be formated in HTML
    email_receiver -- the reciver 
    Return: None
    """
    
    if email_sender == None:
        email_sender = email_receiver

    email_password = password

    subject = f'This is your automated python email'
    body = f"{data}"

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())






if __name__ == "__main__":
    from dotenv import load_dotenv
    import os
    load_dotenv()
    sender = os.getenv("SENDER_EMAIL")
    receiver = os.getenv("RECEIVER_EMAIL")
    password = os.getenv("PASSWORD")
    send_email(email_receiver=receiver,password=password,data="TEST")
