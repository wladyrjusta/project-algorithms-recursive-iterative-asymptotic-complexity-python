from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("ABCDE", 3) == "CBA_ED"
    assert encrypt_message("ABC DE", 2) == "ED C_BA"
    assert encrypt_message("ABCDE", -1) == "EDCBA"
    assert encrypt_message("ABCDE", 9) == "EDCBA"
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(3, "hello world")
