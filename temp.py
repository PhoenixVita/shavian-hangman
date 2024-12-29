myVar = 'b'

word = 'table'
temp = 0

if myVar in word:
    print('yes')

index = word.index(myVar)



print(index)


otherword = 'banana'
otherword = otherword[:index] + word[index] + otherword[index + 1:]
print(otherword)