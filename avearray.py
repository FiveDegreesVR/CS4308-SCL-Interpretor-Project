N = 100
sum= 0
ave= 0
svalue= 0
j= 0
num= 0
varr = [0] * N
num = int(input("Enter number of values to store"))
for j in range(num):
  svalue = float(input("Enter element value: "))
  varr[j]=svalue
sum=0.0
for j in range(num):
  sum = varr[j] + sum
ave=sum/num
print("Average value in array: ",ave)
