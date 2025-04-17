def flatten(nested):
    """Flatten one‑level list of lists."""
    return [x for sub in nested for x in sub]
