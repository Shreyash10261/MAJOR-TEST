def divide(a, b):
    # Intentional bug: does not handle zero division
    return a / b

if __name__ == "__main__":
    print("Result:", divide(10, 0))
