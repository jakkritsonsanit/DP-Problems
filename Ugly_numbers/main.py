def isUgly(n):
    for a in [2, 3, 5]:
        while n % a == 0:
            n = n / a
    return 1 if n == 1 else 0
        
def main(n):
    c = 0
    ans = 1
    while c <= n:
        ans += 1
        
        if isUgly(ans):
            c += 1

    print(ans)
    

if __name__ == "__main__":
    main(int(input()))
