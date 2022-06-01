import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([3,5,7,3])
a2 = np.zeros(10)
a3 = np.ones(10)
a4 = np.random.random(10)
a5 = np.random.randn(10)
a6 = np.linspace(0,10,100)
a7 = np.arange(0,10,0.02)

a1=np.array([2,4,6,8,10])

print(a1[2])
print(a1[2:])
print(a1[:-2])
print(a1[1:-2])
print(a1[a1>3])
names = np.array(['Jim','Luke', 'Josh', 'Pete'])
first_letter_j = np.vectorize(lambda s: s[0](names)=='j')
f = lambda s: s[0]
#f('animal')
names[first_letter_j]
print(a1%4 == 0)
print([ai%4 == 0]
      