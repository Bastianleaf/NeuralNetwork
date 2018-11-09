import random
with open('data_normalizada.data','r+') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()
with open('data_normalizada_random.data','w+') as target:
    for _, line in data:
        target.write( line )