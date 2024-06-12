import math 
h= int(input("enter the h: ")) 
b= int(input("Enter the width: ")) 
d= int(input("Recommended spacing of lights: ")) 
Nx= int(input("The number of grid points along the x direction: "))  
Ny= int(input("The number of grid points along the y direction: ")) 


dictionary={}



for i in range (0,3):
     dictionary["bulb{}".format(i+1)] = (d*i, b/2)



column_points= int(d/Nx)
row_points= int(b/Ny)
z=0
for i in range (0, d+1, column_points):
     for j in range(0, b+1, row_points):
          dictionary["point{}".format(z)]= (i,j)    
          z+=1
print(dictionary)    



sum1=0

for i in range(0, d+1, column_points):
     if i<= d:
          sum1+=1




sum2=3

for i in range(0, b+1, row_points):
     if i<= b:
          sum2+=1

point_amount= sum1* sum2 





choose_point = dictionary[input("enter the point Name: ")]
E = 0
I = 0
sum2 = 3
h = 5
beta = 0

for i in range(0, sum1):
    choose_bulb = dictionary[input("enter the bulb Name: ")]
    dis = math.hypot(choose_point[0] - choose_bulb[0], choose_point[1] - choose_bulb[1])
    alpha = math.degrees(math.atan(dis / h))

    newpoint=(choose_bulb[0], choose_point[1])
    dis2 = math.hypot(newpoint[0] - choose_bulb[0], newpoint[1] - choose_bulb[1])
    beta= (dis2/h)
    print("alpha is : {} and beta is {} ".format(alpha, beta))


    I= float(input("Enter the I :"))
    a= math.radians(alpha)
    E+= (I/ h**2)* math.cos(a)**3


print(" E is : {}".format(E))


