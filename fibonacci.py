def fibonacci():
    """
    Generator that yields Fibonacci numbers.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def main():
    """
    Runs the main program.
    """
    for i, fib in enumerate(fibonacci()):
        print(fib)
        if i == 19:
            break

if __name__ == "__main__":
    main()
