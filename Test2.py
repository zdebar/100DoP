def test():
    b = [0]
    def inner():
        b[0] = 1
    print(b[0])
    inner()
    print(b[0])

test()