# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

#make list of multiples
multiples = []
#for loop for all intergers under 1000
i = 0
for i in range(1000):
#check if divisible by 3
#i/3 is with remainder, i//3 is w/o remainder - if multiple, answer will be same (no r) both times
    if i/3 == i//3:
#check if divisible by 5
#i/5 is with remainder, i//5 is w/o remainder - if multiple, answer will be same (no r) both times
#embed in division of 3 so that there are no repeats
        if i/5 == i//5:
            multiples.append(i)
        if not i/5 == i//5:
            multiples.append(i)
#check divisible by 5 if not divisible by 3
    elif i/5 == i//5:
        multiples.append(i)
    i+1

print(multiples)
#add all multiples in list
sum_multiples = sum(multiples)
print(sum_multiples)