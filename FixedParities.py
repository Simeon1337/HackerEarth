#Simeon D.
#FixedParities
#Hack Solution

def getParity( n ): 
    if n % 2 == 0:
        return 0
    else:
        return 1
 
def main():
    a = int(input())
    
    arr1 = [a]
    arr2 = [a]
    
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    
    b = int(input())
    
    for x in range(0,b):
        row1, col1 =  map(int, input().split())
        row2, col2  = map(int, input().split())

        if getParity(arr1[row1-1] + arr2[col1-1])    ==   getParity(arr1[row2-1] + arr2[col2-1]) :
            print("YES")
        else :
            print("NO")

if __name__ == "__main__":
    main()

