
length = float(input())
breadth = float(input())
height = float(input())
area = length*breadth*height
print(area,length,breadth,height)
print(f"area is {area:.2f}")
print(f"area is {length*breadth*height}")
print(f"it is very {"big" if area>1000 else "small"}")


price = 500.4567
txt = "the price is {:.2f} {} dollars"
print(txt.format(price,price+10))


























