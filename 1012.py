line = raw_input()
line = line.split()

A = float(line[0])
B = float(line[1])
C = float(line[2])

print 'TRIANGULO: {0:.3f}'.format(0.5*A*C)
print 'CIRCULO: {0:.3f}'.format(3.14159*C**2)
print 'TRAPEZIO: {0:.3f}'.format((A+B)*(C/2))
print 'QUADRADO: {0:.3f}'.format(B**2)
print 'RETANGULO: {0:.3f}'.format(A*B)
