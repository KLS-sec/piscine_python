def helper(y, x):
    if y <= x:
        print("Day ", y)
        helper(y + 1, x)


def ft_count_harvest_recursive():
    x = int(input("Days until harvest: "))

    y = 1

    helper(y, x)
    print("Harvest time!")
