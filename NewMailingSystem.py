import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
import config
import os

gmail_id = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('SENDER_EMAIL_PASSWORD')


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def mails(accNo, otp):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(gmail_id, gmail_password)

    from LiteSearchDB import readMailID
    from LiteSearchDB import readName
    email = readMailID(accNo)  # read contacts
    name = readName(accNo)
    message_template = read_template('passwordChange.txt')

    # For each contact, send the email:

    msg = MIMEMultipart()  # create a message

    # add in the actual person name to the message template
    message = message_template.substitute(PERSON_NAME=name.title(), OTP=otp)

    # setup the parameters of the message
    msg['From'] = gmail_id
    msg['To'] = email
    msg['Subject'] = "Banking System"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)
    print("DONE")

    del msg


if __name__ == '__main__':
    mails()
