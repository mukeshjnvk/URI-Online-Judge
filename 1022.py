import fractions
def line(l):
    N1 = int(l[0])
    D1 = int(l[2])
    N2 = int(l[4])
    D2 = int(l[6])
#     print l[6] , n1, n2, d1, d2
    
    if l[3] == '+':
        print '{0}/{1} = {2}/{3}'.format((N1*D2 + N2*D1),(D1*D2), (N1*D2 + N2*D1)/fractions.gcd((N1*D2 + N2*D1),(D1*D2)), (D1*D2)/fractions.gcd((N1*D2 + N2*D1),(D1*D2)))
    elif l[3] == '-':
#         print fractions.gcd((N1*D2 - N2*D1),(D1*D2))
        print '{0}/{1} = {2}/{3}'.format((N1*D2 - N2*D1),(D1*D2), (N1*D2 - N2*D1)/fractions.gcd((N1*D2 - N2*D1),(D1*D2)), (D1*D2)/fractions.gcd((N1*D2 - N2*D1),(D1*D2)))
    elif l[3] == '*':
        print '{0}/{1} = {2}/{3}'.format((N1*N2),(D1*D2), (N1*N2)/fractions.gcd((N1*N2),(D1*D2)), (D1*D2)/fractions.gcd((N1*N2),(D1*D2)))
    elif l[3] == '/':
        print '{0}/{1} = {2}/{3}'.format((N1*D2),(D1*N2), (N1*D2)/fractions.gcd((N1*D2),(D1*N2)), (D1*N2)/fractions.gcd((N1*D2),(D1*N2)))
            


def main():
    t = int(input())
    for i in range(t):
        
        l1 = raw_input()
        l = l1.split(' ')
#         print l
        
        line(l)
    
main()