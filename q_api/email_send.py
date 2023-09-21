# https://hyunmin1906.tistory.com/276
import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "lsh.csc123@gmail.com"
receiver_email = "stout4@naver.com"
password = "hgiwvqjsskkochst"
message = "sdfsdfsdf"

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.encode('utf-8'))

