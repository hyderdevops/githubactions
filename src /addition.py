# app.py
# This is a test commit

def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
