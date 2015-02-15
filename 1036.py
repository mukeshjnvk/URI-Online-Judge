import math
def BhaskarasF(nos):
    A = float(nos[0])
    B = float(nos[1])
    C = float(nos[2])
    
    Delta = float(B**2 - (4*A*C))
    
    
   
    try:
        
        if Delta < 0:
            print 'Impossivel calcular'
                    
        elif Delta == 0:
            print 'R1 = {0:.5f}'.format(-(B)/(2*A))
        else:
            D = math.sqrt(Delta)
            print 'R1 = {0:.5f}'.format((-(B) + D) / ( 2 * A ))
            print 'R2 = {0:.5f}'.format((-(B) - D) / ( 2 * A ))
    except ZeroDivisionError:
        print 'Impossivel calcular'
        


def main():
    nos = raw_input()
    newnos = nos.split(' ')
   
    BhaskarasF(newnos)
    
main()