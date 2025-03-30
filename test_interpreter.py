import pytest
from interpreter import DogLangInterpreter

@pytest.fixture
def interpreter():
    return DogLangInterpreter()

def test_print(capsys, interpreter):
    code = 'гав "Привет, мир!"'
    interpreter.execute(code)
    captured = capsys.readouterr()
    assert "Привет, мир!" in captured.out

def test_variables(capsys, interpreter):
    code = '''
    имя собака "Шарик"
    гав имя
    '''
    interpreter.execute(code)
    captured = capsys.readouterr()
    assert "Шарик" in captured.out

def test_conditions(capsys, interpreter):
    code = '''
    возраст собака 3
    рррр возраст мяу 3:
        гав "Правильно!"
    '''
    interpreter.execute(code)
    captured = capsys.readouterr()
    assert "Правильно!" in captured.out

def test_loops(interpreter):
    code = '''
    счетчик собака 0
    гав-гав счетчик хрю 3:
        счетчик собака счетчик ням 1
    гав счетчик
    '''
    interpreter.execute(code)
    assert interpreter.variables['счетчик'] == 3