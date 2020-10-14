numbers = [1,2]
sum = 0
for i in range(4000000):
    if (i==numbers[-1]+numbers[-2]):
        numbers.append(i)
    
for j in numbers:
    if (j%2 == 0):
        sum += j
    
print(sum)

