from itertools import count 

index = count(0, 0.5)

for i in range(10):
    print(next(index))