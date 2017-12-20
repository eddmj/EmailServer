from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import request
import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

@api_view(['GET'])
def test_server(request):
    if request.method == 'GET':
        return Response('Working', status=status.HTTP_200_OK)


@api_view(['POST'])
def incoming_webhook(request):
    if request.method == 'POST':
        return Response('Working2', status=status.HTTP_200_OK)

@api_view(['GET'])
def send_email(request):
    if request.method == 'GET':
        try:
            # Create message container - the correct MIME type is multipart/alternative.
            msg = MIMEMultipart('alternative')

            msg['From'] = "fromemail@domain.com"
            msg['To'] = "toemail@domain.com"
            msg['Subject'] = "test subject"

            # see the code below to use template as body
            body_text = "Hi this is body text of email"
            body_html = "<p>Hi this is body text of email</p>"

            # Create the body of the message (a plain-text and an HTML version).
            # Record the MIME types of both parts - text/plain and text/html.
            part1 = MIMEText(body_text, 'plain')
            part2 = MIMEText(body_html, 'html')

            # Attach parts into message container.
            # According to RFC 2046, the last part of a multipart message, in this case
            # the HTML message, is best and preferred.
            msg.attach(part1)
            msg.attach(part2)

            # Send the message via local SMTP server.

            mail = smtplib.SMTP("smtp.gmail.com", 587, timeout=20)

            # if tls = True
            mail.starttls()

            recepient = ["edward.millerjones@gmail.com"]

            mail.login("edward.miller@sasystems.com","thisisapassword123")
            mail.sendmail("edward.miller@sasystems.com", recepient, msg.as_string())
            mail.quit()

        except Exception as e:
            raise e