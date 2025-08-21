A python cli todo app deployed to EKS using Github actions 

Add instructions to run the code.
Initially all the todo were saved in a list
Data did not persist , hence stored in files instead of lists.
Function created to read/write to todo.txt
Function to edit and complete to do
clear screen when todos are shown
Unit test to be added
pytest test cases added-> challenge was in setting up pytests.ini
trying to setup github actions to run test automatically when pushing code.
dockerfile was not running correctly
Enter add, show, edit , complete todo or exit/q to exit: Traceback (most recent call last): File "/app/cli.py", line 10, in user_action = (input(user_input)).strip() EOFError: EOF when reading a line
need to run using -it -> docker build -t cli_todo:latest . &
pytest tests were showing red squiggly lines for the import statements in pycharm. This was
fixed by marking the directory as source root.
todo -> add dockerignore file.

