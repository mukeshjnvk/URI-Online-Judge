def test1(nos):
    A = int(nos[0])
    B = int(nos[1])
    C = int(nos[2])
    D = int(nos[3])
    flag = True
 
    
    if B > C and D > A:
        if C + D > A + B:
            if C > 0 and D > 0 and A % 2 == 0:
                print 'Valores aceitos'
            else:
                flag = False
        else:
            flag = False
                
    else:
        flag = False
    if not flag:
        print 'Valores nao aceitos'


def main():
    nos = raw_input()
    newnos = nos.split(' ')
   
    test1(newnos)
    
main()