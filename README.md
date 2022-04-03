I had to make a jenkins pipeline in which we can ingtegrate automate training of machine learning model using jenkins so lets try this !!!!
  
Approach-->>

1). For this I have divided the problem into eight parts i.e. from fetching repo from github to getting a mail into your phone for a successful or unsuccesful result of     trained model\
2). Then I tried to automate the tasks by giving jobs to Jenkins :-\
    job1 - pull the dev code from github repo.\
    job2 - check the env of that ml model is running or not or if not running then run it.\
    job3 - this job will run your training model in python interpreter and check the accuracy of the code.\
    job 4 - this job increase your mode,l accuracy by adding neurons and epochs to your model annd ensure thsat it reach best accuracy of your model.\
    job 5 - it will make you know that your model is not achieving desired accuracy.\
    job6 - if your job acc is greater than 93 this job will send you success mail.\
    job7 - if your job4 didnt get accuracy 93  or fail to run the model then this job will send you model fail mail.\
    job8 - this job is run because in any case your container goes down it will restart the container.

3). My jenkins job is in my article link where I explained all my jobs with screenshots
        <a href="https://medium.com/@akshatjain9782/ml-dev-ops-e6af2869d16e?sk=8caf3968c166c25484c71f510727e5e1" target="_blank">My Article Link:-</a>
        
