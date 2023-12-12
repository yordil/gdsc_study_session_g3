# math_operations.py


def basic_operations(a, b):
    try:
        result = {
            "addition": a + b,
            "subtraction": a - b,
            "multiplication": a * b,
            "division": a / b,
        }
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except Exception as e:
        print("Error:", str(e))
        return None


def power_operation(base, exponent, **kwargs):
    try:
        result = base**exponent
        if "modulo" in kwargs:
            result %= kwargs["modulo"]
        return result
    except Exception as e:
        print("Error:", str(e))
        return None


def apply_operations(operation_list):
    try:
        results = list(map(lambda x: x[0](*x[1]), operation_list))
        return results
    except Exception as e:
        print("Error:", str(e))
        return None


# math_operations.py


def basic_operations(a, b):
    try:
        result = {
            "addition": a + b,
            "subtraction": a - b,
            "multiplication": a * b,
            "division": a / b,
        }
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except Exception as e:
        print("Error:", str(e))
        return None


def power_operation(base, exponent, **kwargs):
    try:
        result = base**exponent
        if "modulo" in kwargs:
            result %= kwargs["modulo"]
        return result
    except Exception as e:
        print("Error:", str(e))
        return None


def apply_operations(operation_list):
    try:
        results = list(map(lambda x: x[0](*x[1]), operation_list))
        return results
    except Exception as e:
        print("Error:", str(e))
        return None


if __name__ == "__main__":
    pass

