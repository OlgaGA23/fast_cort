def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_trace(n, depth=0):
    indent = "  " * depth
    print(f"{indent}fibonacci({n})")

    if n <= 1:
        print(f"{indent} - возвращаем {n}")
        return n

    left = fibonacci_trace(n - 1, depth + 1)
    right = fibonacci_trace(n - 2, depth + 1)
    result = left + right
    print(f"{indent}  -> возвращаем {result}")
    return result

if __name__ == "__main__":
    n = 5
    print(f"fibonacci({n}) = {fibonacci(n)}\n")
    print("стек вызовов для n = 5")
    fibonacci_trace(5)
