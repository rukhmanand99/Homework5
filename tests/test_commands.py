"""
Unit tests for calculator command executions.
"""
import pytest
from app.command import Command

def test_add(invoker):
    """Test addition command."""
    assert invoker.execute("add", 1, 2, 3) == 6

def test_subtract(invoker):
    """Test subtraction command."""
    assert invoker.execute("subtract", 10, 5, 2) == 3

def test_multiply(invoker):
    """Test multiplication command."""
    assert invoker.execute("multiply", 2, 3, 4) == 24

def test_divide(invoker):
    """Test division command and division by zero handling."""
    assert invoker.execute("divide", 10, 2) == 5
    assert invoker.execute("divide", 10, 0) == "Error: Division by zero"
def test_command_abstract_execute():
    """Ensure abstract Command class raises an error when executed."""
    with pytest.raises(NotImplementedError):
        Command().execute()
def test_divide_no_arguments(invoker):
    """Test division when no arguments are provided (should return an error message)."""
    assert invoker.execute("divide") == "Error: Missing arguments"

def test_divide_large_negative_number(invoker):
    """Test division with a large negative number."""
    assert invoker.execute("divide", -100000, 2) == -50000
def test_invoker_invalid_command(invoker):
    """Test invoker executes an invalid command and returns error."""
    assert invoker.execute("unknown", 1, 2) == "Invalid command"
def test_divide_catches_zero_division_error(invoker):
    """Test if ZeroDivisionError is properly caught in divide command."""
    assert invoker.execute("divide", 0, 0) == "Error: Division by zero"
