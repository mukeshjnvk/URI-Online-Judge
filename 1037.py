
def inter(f):
    interv = [ '[0,25]', '(25,50]', '(50,75]', '(75,100]' ]
    interList = [25.0000, 50.0000000, 75.0000000, 100.0000000]
    flag = True
    
    for i in interList:
        if f < 0.0 or f > 100.0:
            flag = False
        elif f <= i:
            inde = interList.index(i)
            
            print 'Intervalo {0}'.format(interv[inde])
            flag = True
            break
          
    
        
    if not flag:
        print 'Fora de intervalo'
            


def main():
    f = float(input())
    inter(f)
    
main()