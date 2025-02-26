from app.invoker import CommandInvoker

def repl():
    invoker = CommandInvoker()

    print("Interactive Calculator - Type 'exit' to quit.")

    while True:
        user_input = input("Enter command: ").strip().split()
        if user_input[0] == "exit":
            break
        try:
            args = list(map(float, user_input[1:]))
            result = invoker.execute(user_input[0], *args)
        except ValueError:
            result = "Invalid input. Please enter numbers."
        print(result)
