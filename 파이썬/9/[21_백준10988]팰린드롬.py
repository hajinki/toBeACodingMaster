n = input()
chars = list(n)

reverse =[]

for i in range (0,len(chars)):
   
    reverse.insert(i, chars[len(chars)-1-i])

if (chars ==reverse):
    print("1")

else: print("0")