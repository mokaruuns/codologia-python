n = int(input())
m = int(input())
s = []
for i in range(n):  # i пробегает 0,1,..,n-1
    s.append([])
    for j in range(m):
        s[i].append(int(input()))
print(s)
