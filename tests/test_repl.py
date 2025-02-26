"""
Unit tests for interactive REPL functionality.
"""
def test_add(invoker):
    """Test addition in REPL."""
    assert invoker.execute("add", 1, 2, 3) == 6

def test_subtract(invoker):
    """Test subtraction in REPL."""
    assert invoker.execute("subtract", 10, 5, 2) == 3

def test_multiply(invoker):
    """Test multiplication in REPL."""
    assert invoker.execute("multiply", 2, 3, 4) == 24

def test_divide(invoker):
    """Test division and division by zero handling in REPL."""
    assert invoker.execute("divide", 10, 2) == 5
    assert invoker.execute("divide", 10, 0) == "Error: Division by zero"
