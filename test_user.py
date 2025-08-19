# test_user.py

import pytest
from src.proj.example import User

def test_username_is_set_correctly():
    user = User("Peter")
    assert user.username == "Peter"

def test_username_defaults_to_random_if_empty():
    user = User("")
    assert user.username == "RANDOM"

def test_username_can_be_changed():
    user = User("Alice")
    user.username = "Bob"
    assert user.username == "Bob"
