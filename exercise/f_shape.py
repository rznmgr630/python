for i in [5,2,5,2,2]:
    print('X'*i)

# second approach
print('=================SECOND APPROACH ==========')
for i in [5,2,5,2,2]:
    output=''
    for j in range(i):
        output+='X';
    print(output);