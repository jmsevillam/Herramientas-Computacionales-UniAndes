list_test=[1,3,8,1.2,6,2,9,3,8,5,10]
print(list_test)
loop=len(list_test)

for i in range(loop-1):
    swapped=False
    for j in range(loop-1):
        if list_test[j] > list_test[j+1]:
            aux=list_test[j]
            list_test[j]=list_test[j+1]
            list_test[j+1]=aux
            swapped=True
    if swapped==False:
        break

print(list_test)
