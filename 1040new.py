import sys
# from select import select


def pro(avg):
    
    if avg > 7.0:
        print ('Aluno aprovado.')
        
    elif avg < 5.0:
        print ('Aluno reprovado.')
        
    elif avg >= 5.0 and avg <= 6.9:
        print('Aluno em exame.')
        
  
#     timeout = 5
#     startTime = time.time()
#     inp = None
    
#     while True:
#         if msvcrt.kbhit():
#             inp = msvcrt.getch()
#             break
#         elif time.time() - startTime > timeout:
#             break
    
    
# #     rlist, wlist, xlist = select([sys.stdin], [], [], timeout)
    
#     if inp:
#         print "Config selected..."
#     else:
#         print "Timed out..."
    
def line2(avg, t):
    # t = float(raw_input())
    print('Nota do exame: {0:.1f}'.format(t))
    
    newavg = (avg+t)/2.0
    
    if newavg >= 5.0:
        
        print ('Aluno aprovado.')
    
    elif avg <= 4.9:
        print ('Aluno reprovado.')
        
    print ('Media final: {0:.1f}'.format(newavg))
    

    
   


def main():
    
    sum = 0.0
    marks = raw_input()
    m = marks.split(' ')

    
    for i in range(4):
        if i == 0:
            sum = sum + float(m[i])*2
           
        elif i == 1:
            sum = sum + float(m[i])*3

        elif i == 2:
        
            sum = sum + float(m[i])*4    

        elif i == 3:
            sum = sum + float(m[i])
        

    avg = sum/10.0
    print ('Media: {0:.1f}'.format(avg))
    
    pro(avg)
    
    l2 = float(raw_input())
    line2(avg, l2)


main()# your code goes here
