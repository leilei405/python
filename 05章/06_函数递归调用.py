def test(n):
    print('num1', n)
    if n > 1:
        test(n - 1)

test(5)