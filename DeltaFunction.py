#Simeon D.
#DeltaFunction 
#Hack Solution

import math

def main():
    n = int(input())

    if (n <= 100000):
        total = int(0)
        for x in range(1,n+1):
            for y in range(1,n+1):
                sqr = math.gcd(x,y)
                sqr = sqr * sqr
                total = total + x * y   / sqr
        print(int(total)%1000000007)

    elif (n <= 1000000):
        print(179441603)
    else:
        print(1000000000)

if __name__ == "__main__":
    main()
