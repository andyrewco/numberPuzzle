from random import *

word_1 = input('Please enter the first word: \n')
word_2 = input('Please enter the second word: \n')
word_3 = input('Please enter the third word: \n')

word_1 =word_1.lower()
word_2 =word_2.lower()
word_3 =word_3.lower()

word_1 = " ".join(word_1)
word_2 = " ".join(word_2)
word_3 = " ".join(word_3)

array_1 = word_1.split()
array_2 = word_2.split()
array_3 = word_3.split()

array_total = array_1 + array_2 + array_3

_size_1 = len(array_1)
_size_2 = len(array_2)
_size_3 = len(array_3)
_size_total = len(array_total)

randNum = 0
number_1 = 1
number_2 = 3
number_3 = 0

while(number_1+number_2 != number_3):
    for x in range(_size_total):
        randNum = randint(0,10) 
        for y in range(x+1,_size_total):
            if not isinstance(array_total[x], int):
                if array_total[y] == array_total[x]:
                    array_total[y] = randNum
        if not isinstance(array_total[x], int):
            array_total[x] = randNum

    def arrayToInt(numList):
        s = ''.join(map(str, numList))
        return int(s)

    array_new_1 = array_total[slice(0,_size_1)]
    array_new_2 = array_total[slice(_size_1,_size_1+_size_2)]
    array_new_3 = array_total[slice(_size_1+_size_2,_size_1+_size_2+_size_3)]

    number_1 = arrayToInt(array_new_1)
    number_2 = arrayToInt(array_new_2)
    number_3 = arrayToInt(array_new_3)

print(array_new_1,number_1)
print(array_new_2,number_2)
print(array_new_3,number_3)


