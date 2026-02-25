def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    # Simple CLI usage: python app.py Hiren
    import sys
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    print(greet(name))
