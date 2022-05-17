import smtplib, ssl


class Email:
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = ""
    receiver_email = ""
    password = ""

    def __init__(self):
        f = open("email.txt", "r")
        self.receiver_email = f.readline()
        self.sender_email = f.readline()
        self.password = f.readline()
        f.close()

    def send(self, subject, message):
        try:
            print("Sending mail.")
            context = ssl.create_default_context()
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(self.sender_email, self.password)
                server.sendmail(self.sender_email, self.receiver_email, "Subject: " + subject + "\n" + message)
            print("Success sending mail.")
        except:
            print("Failed sending mail.")
