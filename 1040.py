import sys
def line(l):
    sum = 0.0
    for i in l:
        sum = sum + float(i)
    
    avg = sum / 4
    
    
    
    print 'Media: {0:.1f}'.format(avg)
    if avg >= 7.0:
        print 'Aluno aprovado.'
    elif avg < 5.0:
        print 'Aluno reprovado.' 
    else:
        print 'Aluno em exame.'
    
    return avg
    
def line2(f, l2):
    print 'Nota do exame: {0}'.format(l2)
    avg = (f + l2) / 2
    if avg >= 5.0:
        print 'Aluno aprovado.'
    else:
        print 'Aluno reprovado.' 
    
    print 'Media final: {0:.1f}'.format(avg)
        
        
   
    
def main():
    
    l1 = raw_input()
    l = l1.split(' ')
    f = line(l)


    l2 = input()
    line2(f, l2)

#     print raw_input()
main()