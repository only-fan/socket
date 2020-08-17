import math

x,y = (input("请输入取值范围：").split(","))

x = int(x)
y = int(y)
             
l = []
for i in range(x,y+1):
    if(i%3 == 0) and (i%5 != 0):
        l.append(str(i))
        
print(",".join(l))
