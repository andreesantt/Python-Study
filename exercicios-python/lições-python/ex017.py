#LEIA OS CATETOS OPOSTO E ADJACENTE E CALCULE A HIPOTENUSA.
from math import pow, sqrt
co = int(input('Digite o cateto oposto: '))
ca = int(input('Digite o cateto adjacente: '))
c1 = pow(co, 2) + pow(ca, 2)
print('sabendo que o cateto oposto vale {} e o adjacente vale {}\nSua hipotenusa vale {:.2f}'.format(co, ca, (sqrt(c1))))

