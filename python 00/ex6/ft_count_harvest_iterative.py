def ft_count_harvest_iterative():
    x = int(input("Days until harvest: "))

    y = range(1, x + 1)
    for n in y:
        print("Day ", n)
    print("Harvest time!")
