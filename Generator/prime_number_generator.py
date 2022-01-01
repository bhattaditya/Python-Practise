"""
returns numbers with even indices in the prime list if 'val' is 0
returns numbers with odd indices in the prime list if 'val' is 1
"""

def primegenerator(num, val):
    # Write your code here
    count = 0
    prime_list = []
    for n in range(2, num):
        for n1 in range(2, n+1):
            if n % n1 == 0:
                count += 1
        if count == 1:
            #print(n, end=' ')  
            prime_list.append(n)
        count = 0         
    
    #print(prime_list[::val+1])
    if val == 1:
        for i in range(0,len(prime_list), 2):
            yield prime_list[i]
            #print(prime_list[i], end =' ')
    if val == 0:
        for i in range(1,len(prime_list), 2):
            yield prime_list[i]
            #print(prime_list[i], end =' ')

if __name__ == "__main__":
     p = primegenerator(100, 0)
     for i in p:
         print(i, end=" ")


