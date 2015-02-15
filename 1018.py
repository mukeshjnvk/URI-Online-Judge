
def change(mon):
    notes = [100, 50, 20, 10, 5, 2]
    print 'NOTAS:'
    r = int(mon[0])
    for n in notes:
        rem = r / n
        if rem > 0:
            print '{0} nota(s) de R$ {1}.00'.format(rem, n)
            r = r - (rem * n)
        else:
            print '{0} nota(s) de R$ {1}.00'.format(rem, n)
    
    mon[1] = int(mon[1]) * 0.01
    if r == 1:
        
        mon[1] = 1 + mon[1]
    change2(mon[1])
            

def change2(r):
    notes = [100, 50, 25, 10, 5, 1]
    r = int(r * 100)
    print 'MOEDAS:'
    for n in notes:
        rem = r / n
        
        if rem > 0:
#             print rem
            print '{0} moeda(s) de R$ {1:.2f}'.format(int(rem), n*.01)
            r = r - (rem * n)
#             print 'r = ',r
        else:
#             print 'r = ',r
            print '{0} moeda(s) de R$ {1:.2f}'.format(int(rem), n*.01)
            
            
            
def main():
    r = raw_input()
    s = r.split('.')
    change(s)
    
    
main()