#4.1
s = 'abcdflgstringn'
print(s[1])
print(s[-1])
print(s[1:3])
print(s.find('e'))
print(s.replace('e', 'E'))
print(s.count('a'))
print(len(s))
print(s.upper())
print(s.lower())
print(s.isdigit())
#4.3.1
string = str(input())
upper = 0
lower = 0
for i in string:
    if i.isupper():
        upper += 1
    else:
        lower += 1
if upper > lower:
    print(string.upper())
else:
    print(string.lower())
#4.3.2
x,y = map(str,input().split())
while not (x.isdigit() and y.isdigit()):
   x,y = map(str,input().split())
print(int(x)+int(y))


