from Email import Email

# How to:
# tutorial at: https://realpython.com/python-send-email/
# create a file in the folder where this script is located: email.txt

# example: email.txt

# receiver@gmail.com
# sender@gmail.com
# sender_password


e = Email()
e.send("Test", "Hallo")
