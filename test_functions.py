import pytest
from functions import *

@pytest.mark.parametrize("filename, expected", [("functions.py", "File opened.")])
def test_openFile_withFile(capsys, filename, expected):
    openFile(filename)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == expected

@pytest.mark.parametrize("filename, expected", [("", "File opened.")])
def test_openFile_withoutFile(capsys, filename, expected):
    with pytest.raises(FileNotFoundError):
        openFile(filename)

@pytest.mark.parametrize("filename, expected", [("lockedFile.txt", "File opened.")])
def test_openFile_withLockedFile(capsys, filename, expected):
    with pytest.raises(PermissionError):
        openFile(filename)

@pytest.mark.parametrize("num1, num2, expected", [(10, 2, 5)])
def test_numbers_withNumbers(num1, num2, expected):
    assert numbers(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [(10.5, 2.5, 4.2)])
def test_numbers_withDecimalNumbers(num1, num2, expected):
    assert numbers(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [("10", "2", "5")])
def test_numbers_withStrings(num1, num2, expected):
    with pytest.raises(TypeError):
        numbers(num1, num2)

@pytest.mark.parametrize("num1, num2, expected", [(10, 0, 5)])
def test_numbers_withZero(num1, num2, expected):
    with pytest.raises(ZeroDivisionError):
        numbers(num1, num2)

@pytest.mark.parametrize("x1, y1, x2, y2, expected", [(3, 2, 2, 2, 1), (0.4, 0.5, 0.8, 0.5, 0.4), (-4, -3, 8, -3, 12)])
def test_dist(x1, y1, x2, y2, expected):
    assert dist(x1, y1, x2, y2) == expected

@pytest.mark.parametrize("x1, y1, x2, y2", [("test", "fail", "pass", "fail")])
def test_dist_string(x1, y1, x2, y2):
    with pytest.raises(TypeError):
        dist(x1, y1, x2, y2)

@pytest.mark.parametrize("values", ["racecar", "Racecar"])
def test_isPalindrome(values):
    assert isPalindrome(values) == True

@pytest.mark.parametrize("values", [5, True])
def test_isPalindrome_type(values):
    with pytest.raises(TypeError):
        isPalindrome(values)

def geninputs():
    inputs = ["5", "10", "0.8", "0.2"]
    for item in inputs:
        yield item

def genstring():
    inputs = ["string", "test"]
    for item in inputs:
        yield item

def genzero():
    inputs = ["4", "0"]
    for item in inputs:
        yield item


GEN = geninputs()
@pytest.mark.parametrize("expected", ["0.5", "4.0"])
def test_divide(capsys, monkeypatch, expected):
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))
    divide()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip().rsplit(" ", 1)[1] == expected

GENS = genstring()
def test_divide_string(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(GENS))
    with pytest.raises(TypeError):
        divide()

GENZ = genzero()
def test_divide_zero(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(GENZ))
    with pytest.raises(ZeroDivisionError):
        divide()

@pytest.mark.parametrize("values, expected", [(9, 3), (0.64, 0.8)])
def test_sq(values, expected):
    assert sq(values) == expected

@pytest.mark.parametrize("values", [(-9)])
def test_sq_negative(values):
    with pytest.raises(ValueError):
        sq(values)

@pytest.mark.parametrize("values", [("25")])
def test_sq_string(values):
    with pytest.raises(TypeError):
        sq(values)     

@pytest.mark.parametrize("first, middle, last, expected", [("John", "Isaac", "Dyess", "Hello!\nWelcome to the program John Isaac Dyess\nGlad to have you!")])
def test_greetUser(capsys, first, middle, last, expected):
    greetUser(first, middle, last)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == expected

@pytest.mark.parametrize("first, middle, last", [(1, 2, 3)])
def test_greetUser_integer(first, middle, last):
    with pytest.raises(TypeError):
        greetUser(first, middle, last)

@pytest.mark.parametrize("first, middle, last", [(True, False, True)])
def test_greetUser_boolean(first, middle, last):
    with pytest.raises(TypeError):
        greetUser(first, middle, last)

@pytest.mark.parametrize("numbers, index, expected", [([1, 2, 3], 1, "Your item at 1 index is 2")])
def test_displayItem(capsys, numbers, index, expected):
    displayItem(numbers, index)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == expected

@pytest.mark.parametrize("numbers, index", [([1, 2, 3], 5)])
def test_displayItem_outofindex(numbers, index):
    with pytest.raises(IndexError):
        displayItem(numbers, index)

@pytest.mark.parametrize("numbers, index", [([1, 2, 3 ], "Fail")])
def test_displayItem_string(numbers, index):
    with pytest.raises(TypeError):
        displayItem(numbers, index)

@pytest.mark.parametrize("numbers, index", [([1, 2, 3 ], 0.5)])
def test_displayItem_decindex(numbers, index):
    with pytest.raises(TypeError):
        displayItem(numbers, index)