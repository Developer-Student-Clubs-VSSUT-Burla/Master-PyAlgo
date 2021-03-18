#compute_inverse in this File , I have declared some functions so as to make the solution non tedious
def egcd(a, b): # // iterative implementation of Extended Euclidean Algorithm (Extended GCD)
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def compute_inverse(a, m):
    g, x, y = egcd(a, m)  #Finding Modular Inverse
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def brute_compute_inverse(a, m):   #This function is not useful much i.e., in the most of the cases
    inv = 0
    for i in range(1, m):
        if (i * a) % m == 1:
            inv = i
            break
    return inv


def main():
    a = int(input("Enter value: "))
    m = int(input("Enter modulo: "))
    print("The inverse of {} (mod {}) is {}".format(a, m, compute_inverse(a, m)))

if __name__ == '__main__':
    main()
#Time complexity
#Function Name	      NLOC	      Complexity	Token
#   egcd	           6              2	         42
#compute_inverse       6    	      2          35
#brute_compute_inverse 7	          3	         37
#main	               4	          1	     40