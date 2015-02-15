

def enc(messg):
    rshift = ''
    for t in messg:
        if t.isalpha():
            rshift = rshift+''.join(chr(ord(t) + 3))
        else:
            rshift = rshift+''.join(t)
#     print rshift
    revrshift = rshift[-1::-1]
#     print revrshift
    m = len(revrshift)/2
    finrevrshift = revrshift[:m]
#     print finrevrshift
    for i in range(m, len(revrshift)):
        finrevrshift =  finrevrshift+''.join(chr(ord(revrshift[i]) - 1))
    print finrevrshift

def main():
    t = int(input())
    
    for i in range(t):
        ptext = raw_input()
        
        enc(ptext)
        
    
main()