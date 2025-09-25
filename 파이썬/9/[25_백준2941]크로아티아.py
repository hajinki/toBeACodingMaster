n = input(",")
chars = list(n)
num=0

alpha = ["q","w","e","r","t","y","u","i","o","p","a","f","g","h","j","k","x","v","b","m"]

croatia = ["c=","c-","dz=","d-","lj","nj","s=","z="]


# 일단 한글자씩 글자 꺼내서 반복
i=0
while i < len(chars):
    if chars[i] in alpha:
        num+=1
        i+=1
    else:
        ctr=str(chars[i])+str(chars[i+1])
        ctr3=str(chars[i])+str(chars[i+1])+str(chars[i+2])
        if ctr in croatia:
            num+=1
            i+=2
        else: 
            if ctr3 in croatia:
                num+=1
                i+=2
            else:
                num+=2
                i+=1    
print (num)



# 만약에 일반 알파벳이면 +1
# 앞뒤 따졋슬때 크로아티아? +1
# n, n+1
# 그러면 일단 c,d,l,n,s,z 면 일단 +1하지말고 다음글자까지 읽
# 다을글자까지 합쳤을때 크로아티아? 그럼 +1
# 다음글자와의 조합이 크로아티아 아님? 그럼 +2