#first file
def first(p, q):
    if p == 0:
        return q, 0, 1
    else:
        k, s, r = first(q % p, p)
        return k, r - (q // p) * s, s

def const(p, c):
    k, r, s= first(p, c)
    if k != 1:
        raise Exception('modular inverse does not exist')
    else:
        return r % c

def const2(p, c):
    temp = 0
    for z in range(1, c):
        if (z * p) % c == 1:
            temp = z
            break
    return temp


def main():
    p = int(input("Enter value: "))
    c = int(input("Enter modulo: "))
    print("The inverse of {} (mod {}) is {}".format(p, c, const(p, c)))

if __name__ == '__main__':
    main()