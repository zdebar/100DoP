def binariez(a):
    assert int(a) == a and int(a) >= 0, "No valid input"
    if a == 1:
        return "1"
    return  binariez(a//2) + str(a % 2)

B
print(binariez(1156))
