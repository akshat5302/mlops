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
Subject: Model training  for the built is done successfully 
Hello,
      Developer this is email regarding to your training of the model. The accuracy of your model has been checked and it seems that the model has given the best accuracy
                                                       THANK YOU'''

#SENDING THE MAIL

s.sendmail(sender_email,receiver_email , message)

#terminating the session
s.quit()
