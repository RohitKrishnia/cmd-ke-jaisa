a=0
b=0
c=0
d=0
e=0
f=0
su=0
for a in range(0,13):
    for b in range(0,13):
        for c in range(0,13):
            for d in range(0,13):
                if(a**3+b**3==c**3+d**3):
                    
                        if(a==b or b==c or c==d or d==a or b==d or c==a):
                            
                            continue
                        else:
                           e=a
                           f=b
                            
                            
print(e**3+f**3)
