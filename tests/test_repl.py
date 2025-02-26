import pytest
from app.repl import repl

def test_repl_execution(monkeypatch, capsys):
    """Test REPL execution with simulated user input, including edge cases."""
    inputs = iter([
        "add 1 2",        # Normal addition
        "subtract 5 2",   # Normal subtraction
        "multiply 3 3",   # Normal multiplication
        "divide 10 2",    # Normal division
        "invalid",        # Triggers ValueError (Line 11)
        "exit"            # Exits REPL (Lines 15-16)
    ])
    
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    repl()  # Run the REPL with simulated input
    
    captured = capsys.readouterr()
    
    assert "3.0" in captured.out  # add 1 + 2
    assert "3.0" in captured.out  # subtract 5 - 2
    assert "9.0" in captured.out  # multiply 3 * 3
    assert "5.0" in captured.out  # divide 10 / 2
    assert "Invalid input. Please enter numbers." in captured.out  # Triggers Line 11 (ValueError)
    assert "Interactive Calculator - Type 'exit' to quit." in captured.out  # Ensures REPL starts

def test_repl_exit(monkeypatch, capsys):
    """Test if REPL properly exits when 'exit' is entered."""
    inputs = iter(["exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    repl()  # Run the REPL

    captured = capsys.readouterr()
    
    assert "Interactive Calculator - Type 'exit' to quit." in captured.out  # Ensures REPL starts
