#sum even and odd digits and print
n=int(input())
sum_even=0
sum_odd=0 
while n>0:
     rem=n%10
     if rem%2==0:
          sum_even+=rem
     else:
          sum_odd+=rem
     n=n//10
print(sum_even,end=' ')
print(sum_odd)