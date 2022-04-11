a = 17391
b = 546
c = 934
a = a%17
b = b%17
c = c%17
print(a,b,c)
if a<b<c or a<c<b:
	print(a,"- самый маленький остаток")
elif c<a<b or c<b<a:
	print(c,"- самый маленький остаток")
elif b<a<c or b<c<a:
	print(b,"- самый маленький остаток")
else: 
	print("ERROR")
