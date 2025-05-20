from flashcard import Flashcard

def test_ask_correct(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Paris")

    fc = Flashcard("What is the capital of France?", "Paris")
    assert fc.ask() == True

def test_ask_incorrect(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "London")

    fc = Flashcard("What is the capital of France?", "Paris")
    assert fc.ask() == False