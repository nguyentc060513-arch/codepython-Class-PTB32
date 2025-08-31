t = 0 
for i in range(2, 100): 
    nguyen_to = True 
    for J in range(2, i):
        if i%J == 0: 
          nguyen_to = False 
          break 
    if nguyen_to: 
       print(i, end="") 
       t += i 
print("tong cac so nguyen to nho hon 100 la: ", t ) 


# 1.b 
# 2.a 
# 3.a 
# 4.c 
# 5.c 
#6.c 
#7.c 
#8.a 
#9.b 
#10.c