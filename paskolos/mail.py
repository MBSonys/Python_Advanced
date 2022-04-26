import smtplib
from email.message import EmailMessage
from password import passwordas

def sending_email(loan_email, email_info, email_graph):
    email = EmailMessage()
    email['from'] = 'Jusu mylimas bankas'
    email['to'] = f'{loan_email}'
    email['subject'] = 'Your loan info'

    email.set_content(f"Hello, your loan info: {email_info}, graph {email_graph}")

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('zppython10@gmail.com', passwordas)
        smtp.send_message(email)