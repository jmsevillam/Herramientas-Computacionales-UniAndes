NumberTest=777071
Prime=True
for i in range(2,NumberTest):
    if NumberTest%i==0:
        Prime=False
        break
if Prime:
    print('The Number is Prime')
else:
    print('The Number is not Prime')
