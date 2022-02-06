R = int(input("Enter the number of rows: "))
C = int(input("Enter the number of columns: "))
r = int(input("Enter row index: "))
c = int(input("Enter column index: "))
s = r*C+c
print(s)


R = int(input("Enter the number of rows: "))
C = int(input("Enter the number of columns: "))
s = int(input("Enter index: "))
c = s % C
r = int((s-c)/C)
print(r, c)

X_1 = int(input("Enter dimension 1 length: "))
X_2 = int(input("Enter dimension 2 length: "))
X_3 = int(input("Enter dimension 3 length: "))
x_1 = int(input("Enter index for dimension 1: "))
x_2 = int(input("Enter index for dimension 2: "))
x_3 = int(input("Enter index for dimension 3: "))
s = (x_1*X_2+x_2)*X_3+x_3
print(s)


X_1 = int(input("Enter dimension 1 length: "))
X_2 = int(input("Enter dimension 2 length: "))
X_3 = int(input("Enter dimension 3 length: "))
s = int(input("Enter index: "))
x_3 = s % X_3
x_2 = (s-x_3)/X_3 % X_2
x_3 = ((s-x_3)/X_3 - x_2)/X_2
print(x_1,x_2,x_3)








