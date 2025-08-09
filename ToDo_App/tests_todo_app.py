import pytest
from todo_functions import *

TEST_FILE = 'test_todos.txt'


def test_save_todos():
    add_todos('new_todo', cli_app=True, filepath=TEST_FILE)
    assert get_todos(TEST_FILE)[0] == "new_todo"
    print(get_todos(filepath=TEST_FILE))

# def test_complete_todos():
#     modify_todo(action='complete', new_todo', cli_app=True, filepath=TEST_FILE)
#     assert get_todos(TEST_FILE)[0] == "new_todo"
#     print(get_todos(filepath=TEST_FILE))