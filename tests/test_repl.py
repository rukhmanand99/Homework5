import pytest
from app.repl import repl

def test_repl_execution(monkeypatch, capsys):
    """Test REPL execution with simulated user input."""
    inputs = iter(["add 1 2", "subtract 5 2", "multiply 3 3", "divide 10 2", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    repl()  # Run the REPL with simulated input
    
    captured = capsys.readouterr()
    
    assert "3.0" in captured.out  # add 1 + 2
    assert "3.0" in captured.out  # subtract 5 - 2
    assert "9.0" in captured.out  # multiply 3 * 3
    assert "5.0" in captured.out  # divide 10 / 2
