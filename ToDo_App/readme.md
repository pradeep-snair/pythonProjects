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
