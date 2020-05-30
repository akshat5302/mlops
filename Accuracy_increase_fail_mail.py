import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication

sender_email = "akshatjain9782@gmail.com"
sender_password = "Akshat@123"
receiver_email = "tanishqjain7014@gmail.com"
s.login(sender_email, sender_password)

# message to be sent

message = '''\
Subject: Accuracy increase for the built has been failed 
Hello,
      Developer this is email regarding to your accuracy of the model. it seems that your Accuray_increase.py is not working please check and recommit it
                                         THANK YOU'''

#SENDING THE MAIL

s.sendmail(sender_email,receiver_email , message)

#terminating the session

s.quit()