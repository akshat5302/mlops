task given to us by vimal sir : we have to make a jenkins model in which we can ingtegrate machine learning mode using jenkins
solution 
for this i have created eight jobs
job1 - pull the dev code from github repo
job2 - check the env of that ml model is running or not or if not running then run it
job3 - this job will run your training model in python interpreter and check the accuracy of the code
job 4 - this job increase your mode,l accuracy by adding neurons and epochs to your model annd ensure thsat it reach best accuracy of your model
job 5 - it will make you know that your model is not achieving desired accuracy
job6 - if your job acc is greater than 93 this job will send you success mail
job7 - if your job4 didnt get accuracy 93  or fail to run the model then this job will send you model fail mail
job8 - this job is run because in any case your container goes down it will restart the container
