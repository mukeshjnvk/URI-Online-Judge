
import string


def fun(line):
    if line[0] in line[1] :
        r = line[0]
        l = line[1].replace(r, '')
        if l == '':
            print 0
        else:
            print int(l)
    
    else:
        print line[1]

def inp():
    
    
    line = raw_input()
    line = line.split()
    
    if line[0] != '0' and line[1] != '0':
        fun(line)
        return True
    else:
        return False
    
def main():
    flag = True
    
    while flag:
        flag = inp()
   
        
main()