
def find(n,string):
    w_count ,i_count,s_count,h_count = 0,0,0,0

    for char in string:
        if char == "w":
            w_count += 1
        elif char == "i":
            i_count += 1
        elif char == "s":
            s_count += 1
        elif char == "h":
            h_count += 1

    min_req = min(w_count,i_count,s_count,h_count)
    print(min_req)

n = 8
string = "wishwish"
find(n,string)























