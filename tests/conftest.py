"""
Configuration file for pytest fixtures.
This file ensures test dependencies and reusable components are available.
"""
import pytest
from app.invoker import CommandInvoker
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multipy import MultiplyCommand
from app.commands.divide import DivideCommand

@pytest.fixture(scope="module")
def invoker():
    """Creates an instance of CommandInvoker with registered commands."""
    invoker = CommandInvoker()
    invoker.register("add", AddCommand())
    invoker.register("subtract", SubtractCommand())
    invoker.register("multiply", MultiplyCommand())
    invoker.register("divide", DivideCommand())
    return invoker
