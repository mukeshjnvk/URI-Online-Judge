import signal



def pro(avg):
    
    if avg > 7.0:
        print ('Aluno aprovado.')
        
    elif avg < 5.0:
        print ('Aluno reprovado.')
        
    elif avg >= 5.0 and avg <= 6.9:
        print('Aluno em exame.')
        
       
   
      
def line2(avg, t):
    # t = float(raw_input())
    print('Nota do exame: {0:.1f}'.format(t))
    
    newavg = (avg+t)/2.0
    
    if newavg >= 5.0:
        
        print ('Aluno aprovado.')
    
    elif avg <= 4.9:
        print ('Aluno reprovado.')
        
    print ('Media final: {0:.1f}'.format(newavg))
    

    
def input1():
    try:
        print 'You have 5 seconds to type in your stuff...'
        foo = raw_input()
        return foo
    except:
        # timeout
        return


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
    
    
    
    
    
    
    
   
    TIMEOUT = 5 # number of seconds your want for timeout
    
#     def interrupted(signum, frame):
#         "called when read times out"
#         print 'interrupted!'
#     signal.signal(signal.SIGALRM, interrupted)
    
    
    
    # set alarm
    signal.alarm(TIMEOUT)
    s = raw_input1()
    # disable the alarm after success
    signal.alarm(0)
#     print 'You typed', s

    if s != 'None':
        line2(avg, float(s))
    


main()



