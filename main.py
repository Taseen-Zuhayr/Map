num1 = [1,2,3,4,5]
num2 = [6,7,8,9,10]
res = map(lambda x,y: x+y, num1,num2) #Comprihension
print(list(res))

num = [1,2,3,4,5]
def square(n):
    return n**2
sq = list(map(square,num))
print(sq)

