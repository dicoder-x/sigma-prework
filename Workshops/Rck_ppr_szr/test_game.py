from game import *


def user_choice(choices: list, monkeypatch) -> None:
    """
    Take a list of choices and uses them to feed into the game to test with
    Monkeypatch is used to fake (or 'mock') the input from the user
    """
    answers = iter(choices)
    monkeypatch.setattr('builtins.input', lambda name: next(answers))


def test_victor():
    assert victor("rock", "paper") == "You lose!"
    assert victor("rock", "scissors") == "You win!"
    assert victor("rock", "rock") == "It's a tie!"


def test_check_valid():
    assert victor("rock", "paper") == "You lose!"
    assert victor("rock", "scissors") == "You win!"
    assert victor("rock", "rock") == "It's a tie!"


def test_user_choice(monkeypatch, capsys):
    user_choice(["", "wizard", "RoCk"], monkeypatch)
    main()
    captured_output = capsys.readouterr().out
    assert "rock" in captured_output
