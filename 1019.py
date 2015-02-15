
def timef(s):
    
   
    
    y = s / 365
    if y > 0:
        s = s % 365
    m = s / 30
    if m > 0:
        d = s % 30
    
    print '{0} ano(s)\n{1} mes(es)\n{2} dia(s)'.format(y, m, d)
   


def main():
    s = int(input())
    
    timef(s)
    
main()