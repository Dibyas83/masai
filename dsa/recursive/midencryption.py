
def encrypt(n,sti,start,end):
    ans = ""
    if start > end:
        return ans
    mid = (start + end) // 2
    ans += sti[mid]

    return ans + encrypt(n, sti, start, mid-1) + encrypt(n, sti, mid + 1, end) # functions giving mid as ans at every step

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        sti = input().strip()
        print(encrypt(n,sti,0,n-1))

if __name__== "__main__":
    main()










