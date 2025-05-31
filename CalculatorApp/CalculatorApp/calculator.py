import logging
from database import log_to_db
from logger_config import setup_logger

logger = setup_logger()

def add(a, b):
    result = a + b
    logger.info(f"Added {a} + {b} = {result}")
    log_to_db("Addition", a, b, result)
    return result

def subtract(a, b):
    result = a - b
    logger.info(f"Subtracted {a} - {b} = {result}")
    log_to_db("Subtraction", a, b, result)
    return result

def multiply(a, b):
    result = a * b
    logger.info(f"Multiplied {a} * {b} = {result}")
    log_to_db("Multiplication", a, b, result)
    return result

def divide(a, b):
    try:
        result = a / b
        logger.info(f"Divided {a} / {b} = {result}")
        log_to_db("Division", a, b, result)
        return result
    except ZeroDivisionError:
        logger.error("Attempted to divide by zero.")
        return "Error: Division by zero"

def main():
    print("Simple Calculator
Type 'exit' to quit")
    while True:
        try:
            a = input("Enter first number: ")
            if a == "exit": break
            b = input("Enter second number: ")
            if b == "exit": break
            op = input("Enter operation (+, -, *, /): ")
            if op == "exit": break

            a, b = float(a), float(b)

            if op == '+':
                print("Result:", add(a, b))
            elif op == '-':
                print("Result:", subtract(a, b))
            elif op == '*':
                print("Result:", multiply(a, b))
            elif op == '/':
                print("Result:", divide(a, b))
            else:
                print("Invalid operation")

        except ValueError:
            print("Please enter valid numbers")

if __name__ == "__main__":
    main()
