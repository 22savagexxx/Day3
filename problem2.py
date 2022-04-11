a = input("Введите первое число: ")
b = input("Введите второе число: ") 
c = input("Введите третье число: ")
print(a,b,c)
if a>b>c or a>c>b:
	print("Самое большое число: ", a)
elif b>a>c or b>c>a:
	print("Самое большое число: ", b)
elif c>a>b or c>b>a:
	print("Самое большое число: ", c) 
else:
	print("ERROR")
if a<b<c or a<c<b:
        print("Самое маленькое число: ", a)
elif b<a<c or b<c<a:
        print("Самое маленькое число: ", b)
elif c<a<b or c<b<a:
        print("Самое маленькое число: ", c) 
else:
        print("ERROR")


