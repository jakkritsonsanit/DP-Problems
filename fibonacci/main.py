def fib(n: int):

    fibs = [0, 1]

    for i in range(2, n+1):
        fibs.append(fibs[i - 1] + fibs[i - 2])

    return fibs[-1]

def main():
    n = int(input())

    print(fib(n))


if __name__ == "__main__":
    main()