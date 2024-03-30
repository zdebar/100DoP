a = ["computer"]
b = a 

def test(testa):
    c = testa[:]
    c.append(4)
    return c



print(a)
print(test(a))
print(a)