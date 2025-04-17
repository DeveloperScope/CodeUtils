def fact(n):
    """Very naive factorial (no input validation)."""
    return 1 if n <= 1 else n * fact(n - 1)
