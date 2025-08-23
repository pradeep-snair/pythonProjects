Comments 

1. Add instructions to run the code. 
2. Initially all the todo were saved in a list
3. Data did not persist , hence stored in files instead of lists. 
4. Function created to read/write to todo.txt
5. Function to edit and complete to do
6. clear screen when todos are shown
7. Unit test to be added 
8. pytest test cases added-> challenge was in setting up pytests.ini 
9. trying to setup github actions to run test automatically when pushing code.
10. dockerfile was not running correctly 
    1. Enter add, show, edit , complete todo or exit/q to exit: Traceback (most recent call last):
       File "/app/cli.py", line 10, in <module>
       user_action = (input(user_input)).strip()
       EOFError: EOF when reading a line
    2. need to run using -it -> docker build -t cli_todo:latest . & 
    3. pytest tests were showing red squiggly lines for the import statements in pycharm. This was
    4. fixed by marking the directory as source root. 
    5. todo -> add dockerignore file. 

Docker Push error - tag name was wrong. 
When changing the folder name I did not name it correctly and the github actions failed. 
Pushing the image with the SHA tag to docker hub is failing. 

Split the Giuthub actions file into 3 jobs
checkout code was not done in docker build job which gave the error ->     - name: Checkout code
      uses: actions/checkout@v3 

Kubernetes pod gives this error though docker container runs 
fine File "/app/cli.py", line 10, in <module> user_action = (input(user_input)).strip()
this error is fixed by adding the lines in 
    image: pradsn/todo-app
        stdin: true
        tty: true
        ports:

kubectl exec -it todo-cli -- python cli.py

initially created the cluster manually 
then added the job to deploy the pods to cluster

Need to add code to create the cluster automatically  
