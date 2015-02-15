
def coor(l):
    x = float(l[0])
    y = float(l[1])
    
    if x == 0.0:
        if y == 0.0:
            print 'Origem'
        else:
            print 'Eixo Y'
            
    elif y == 0.0:
        if x != 0.0:
            print 'Eixo X'
            
    elif x > 0.0:
        if y > 0.0:
            print 'Q1'
        else:
            print 'Q4'
    elif x < 0.0:
        if y > 0.0:
            print 'Q2'
        else:
            print 'Q3'
            

def main():
    
    l1 = raw_input()
    l = l1.split(' ')
    coor(l)
    
main()