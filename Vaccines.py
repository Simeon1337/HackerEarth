#Simeon D.
#Finding Vaccines
#HackerEarth - August Easy - 100/100

from collections import OrderedDict

def main():
    n = int(input())
    len_input = int(input())
    virus = input()
 
    G1,C1 = 0,0
 
    for char in virus:
        if (char == 'G'):
            G1+=1
        elif (char == 'C'):
            C1+=1

    Viruses = {}
 
    for i in range(1,n+1):
        t1 = int(input())
        virus = input()
 
        G2,C2 = 0,0

        for char in virus:
            if (char == 'G'):
                G2+=1
            elif (char == 'C'):
                C2+=1
        
        v = (C1 * G2) + (G1 * C2)  #calculates interactions
        Viruses.update({i:v})  #enters dictionary values
    
    Sorted_Viruses = sorted(Viruses, key=Viruses.get, reverse=True)  # sort dictionary by descending values
 
    print(Sorted_Viruses[0])  #print first dictionary key (vaccine)
 
if __name__ == '__main__': 
    main()