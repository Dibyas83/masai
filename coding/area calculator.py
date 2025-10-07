while True:
    print("1 for sqare area\n"
          "2 for circle\n"
          "3 for triangle\n"
          "print other nums to stop")
    choice = input()
    if choice == "1":
        while True:
            side = float(input("side length = "))
            area = side ** 2
            print(area)
            p = input("want to calculate again press y/n: ")
            if p == "n":
                break
    elif choice == "2":
        while True:
            side = float(input("side length = "))
            area = 3.14 * side ** 2
            print(area)
            p = input("want to calculate again press y/n: ")
            if p == "n":
                break
    elif choice == "3":
        while True:
            side1 = float(input("base length = "))
            side2 = float(input("height length = "))
            area = side2 * side1 * 1 / 2
            print(area)
            p = input("want to calculate again press y/n: ")
            if p == "n":
                break
    else:

        break











