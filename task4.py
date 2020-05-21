sample = {'physics' : 88,
           'maths' :75,
           'chemistry' :72,
           'Basic electrical' :89}
a=min(sample.values())
for i in sample:
    if a == sample[i]:
        print(i)
