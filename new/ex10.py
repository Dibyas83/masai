def solve(N):
  if N >0 & N<1000:
    N=N*3
    N=N+10
    print(N)


def update_number(number):
    if number <= 30 & number >= 1:
        number *= 3
        number += 7
        number -= 10
    print(number)

    def calculate_product(one, two, three, four, five, six):


        product = 1
        for i in (one, two, three, four, five, six):
            product *= i
        print(product)