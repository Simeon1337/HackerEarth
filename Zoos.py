#Simeon D.
#Zoos

def main():
    n = input()
    
    count1 = 0
    count2 = 0
    for x in n:
        if x == 'z':
            count1 += 1
        else:
            count2 += 1
    
    if (count2 / count1) == 2:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()