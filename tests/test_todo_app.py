import pytest

from todo_functions import (
    add_todos,
    get_todos,
    save_todos,
    check_valid_todo,
    complete_todo_gui,
    modify_todo,
    show_todos
)


# Test add_todos and get_todos
def test_add_and_get_todos(tmp_path):
    test_file = tmp_path / "test_todos.txt"
    add_todos("Buy milk\n", filepath=str(test_file))
    add_todos("Walk dog\n", filepath=str(test_file))
    todos = get_todos(filepath=str(test_file))
    assert todos == ["Buy milk\n", "Walk dog\n"]


# Test save_todos
def test_save_todos(tmp_path):
    test_file = tmp_path / "test_todos.txt"
    todos = ["Task 1\n", "Task 2\n"]
    save_todos(todos, filepath=str(test_file))
    with open(test_file, 'r') as f:
        saved = f.readlines()
    assert saved == todos


# Test check_valid_todo
def test_check_valid_todo(tmp_path, capsys):
    test_file = tmp_path / "test_todos.txt"
    save_todos(["Task 1\n"], filepath=str(test_file))

    assert not check_valid_todo("Task 1\n", filepath=str(test_file))  # Duplicate
    captured = capsys.readouterr()
    assert "already present" in captured.out

    assert not check_valid_todo("   ", filepath=str(test_file))  # Empty
    captured = capsys.readouterr()
    assert "Enter a valid todo" in captured.out

    assert check_valid_todo("New Task\n", filepath=str(test_file))  # Valid


# # Test complete_todo_gui
# def test_complete_todo_gui(tmp_path):
#     test_file = tmp_path / "test_todos.txt"
#     save_todos(["Task 1\n", "Task 2\n"], filepath=str(test_file))
#     complete_todo_gui("Task 1\n", filepath=str(test_file))
#     todos = get_todos(filepath=str(test_file))
#     assert todos == ["Task 2\n"]


# Test modify_todo: complete
def test_modify_todo_complete(tmp_path, monkeypatch, capsys):
    test_file = tmp_path / "test_todos.txt"
    save_todos(["Task 1\n", "Task 2\n"], filepath=str(test_file))

    monkeypatch.setattr("builtins.input", lambda _: "1")
    monkeypatch.setattr("todo_functions.clear_screen", lambda: None)
    monkeypatch.setattr("todo_functions.show_todos", lambda filepath=test_file: None)

    modify_todo("complete", filepath=str(test_file))
    todos = get_todos(filepath=str(test_file))
    assert todos == ["Task 2\n"]


# Test modify_todo: edit
def test_modify_todo_edit(tmp_path, monkeypatch, capsys):
    test_file = tmp_path / "test_todos.txt"
    save_todos(["Task 1\n"], filepath=str(test_file))

    monkeypatch.setattr("builtins.input", lambda prompt: "1" if "number" in prompt else "Updated Task")
    monkeypatch.setattr("todo_functions.clear_screen", lambda: None)
    monkeypatch.setattr("todo_functions.show_todos", lambda filepath=test_file: None)

    modify_todo("edit", filepath=str(test_file))
    todos = get_todos(filepath=str(test_file))
    assert todos == ["Updated Task\n"]


# Optional: Test show_todos output
def test_show_todos_output(tmp_path, capsys):
    test_file = tmp_path / "test_todos.txt"
    save_todos(["Task A\n", "Task B\n"], filepath=str(test_file))
    show_todos(filepath=str(test_file))
    captured = capsys.readouterr()
    assert "Task A" in captured.out
    assert "Task B" in captured.out
