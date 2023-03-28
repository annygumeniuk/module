import pytest
from main import parse_lines, check_positive
import os

def test_age():
    lines = parse_lines()
    element = lines[0]
    age = element['age']
    assert age < 50


def test_name():
    lines = parse_lines()
    element = lines[2]
    name = element['FirstName']
    assert name == 'Aria'


def test_positive():
    lines = parse_lines()
    result = check_positive(lines)
    assert result == 'There are 3 positive characters'

