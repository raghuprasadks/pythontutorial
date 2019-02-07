# -*- coding: utf-8 -*-
mylist=[3,4,9,8,2]
sumEven=0
sumOdd=0
for ele in mylist:
    print(ele)
    if(ele%2==0):
       sumEven+= ele
    else:
        sumOdd+=ele

print('Sum  even ',sumEven) 
print('Sum  odd ',sumOdd)