line1 = raw_input()
line1 = line1.split()

line2 = raw_input()
line2 = line2.split()

print 'VALOR A PAGAR: R$ {0:.2f}'.format((int(line1[1]) * float(line1[2])) +  (int(line2[1]) * float(line2[2])))