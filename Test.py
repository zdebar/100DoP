nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]


def contains_duplicate(a):
    seen = set()
    count = 0
    for i in a:
        if i in seen: return True
        seen.add(i)
        count += 1
        print(f"Step {count}")
    return False


print(contains_duplicate(nums))