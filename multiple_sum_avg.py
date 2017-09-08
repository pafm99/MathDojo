#MULTIPLES

#PART 1
#for x in range (1, 1000, 2): #(start, end, step)
#    print x 

#PART 2
#for x in range (5, 1000000, 5):
#    print x

#SUM LIST
a = [1, 2, 5, 10, 255, 3]
print sum(int(x) for x in a)

#AVERAGE LIST
print sum(int(x) for x in a) / len(a)
    
