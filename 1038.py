
def line(l):
    x = int(l[0])
    y = int(l[1])
    
    price = [4.00, 4.50, 5.00, 2.00, 1.50]
    print 'Total: R$ {0:.2f}'.format(price[x-1] * y)
    
    
    
def main():
    
    l1 = raw_input()
    l = l1.split(' ')

    
    line(l)

main()