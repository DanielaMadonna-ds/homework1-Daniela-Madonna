#Introduction:Say "Hello,World!"
if __name__ == '__main__':
    print("Hello, World!")
#Python if-Else
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a + b)
print(a - b)
print(a * b)

#Python:Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print(a//b)
print(a/b)

#Loops
if __name__ == '__main__':
    n = int(input())

for i in range(n):
    print(i ** 2)

#Print Function
if __name__ == '__main__':
    n = int(input())
    
for i in range (1, n+1):
    print(i, end='')

#Write a function
def is_leap(year):
    leap = False
    if year % 400 == 0:
        return True 
    elif year % 100 == 0:
        return False 
    elif year % 4 == 0:
        return True
    else:
        return False
    
    return leap

year = int(input())
print(is_leap(year))

#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])

#Find the Runner-up score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
nuova_lista = sorted(set(arr))
print(nuova_lista[-2])

#Nested Lists
if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        records.append([name, score])
    
    voti = sorted(set([student[1] for student in records]))
    
    second_lowest = voti[1]
    students_filtred = sorted(student[0] for student in records if student[1] == second_lowest)
    
    for name in students_filtred:
        print(name)

#Finding the percentage 
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    voti = student_marks[query_name]
    media = sum(voti) / len(voti)
    print(f"{media:.2f}")

#Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    t = tuple(integer_list)
    print(hash(t))

#Lists
if __name__ == '__main__':
    N = int(input())
    arr = []
    
    for i in range(N):
        command = input().split()
        cmd = command[0]
        
        if cmd == "insert":
            arr.insert(int(command[1]), int(command[2]))
        elif cmd == "print":
            print(arr)
        elif cmd == "remove":
            arr.remove(int(command[1]))
        elif cmd == "append":
            arr.append(int(command[1]))
        elif cmd == "sort":
            arr.sort()
        elif cmd == "pop":
            arr.pop()
        elif cmd == "reverse":
            arr.reverse()

#Swap case
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#String Split and Join
def split_and_join(line):
    # write your code here
    return "-".join(line.split(" "))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#What's Your Name?
def print_full_name(first, last):
    # Write your code here
    first = first_name
    last = last_name
    print("Hello" , first , last + "!", "You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#Mutations
def mutate_string(string, position, character):
   return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#Find a string 
def count_substring(string, sub_string):
    count = 0 
    for i in range (len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count 

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

#String Validators
if __name__ == '__main__':
    s = input()
    has_alnum = False
    for i in s:
        if i.isalnum():
            has_alnum = True
            break
    print(has_alnum)
    
    has_alpha = False
    for i in s:
        if i.isalpha():
            has_alpha = True
            break
    print(has_alpha)
    
    has_digit = False
    for i in s:
        if i.isdigit():
            has_digit = True
            break
    print(has_digit)
    
    has_lower = False
    for i in s:
        if i.islower():
            has_lower = True
            break
    print(has_lower)
    
    has_upper = False
    for i in s:
        if i.isupper():
            has_upper = True
            break
    print(has_upper)

#Text Alignment
thickness = int(input()) #This must be an odd number
c = 'H'
#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    
#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    
#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#Text Wrap
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#Designer Door Mat
N,M = map(int, input().split())

#upper part  
for i in range(1, N, 2):
    print(('.|.'*i).center(M, "-"))

#central part  
print('WELCOME'.center(M, '-'))

#lower part 
for i in range(N-2, -1,-2):
    print(('.|.' * i).center(M, '-'))

#String Formatting 
def print_formatted(number):
    # your code goes here
    width = len(bin(n)[2:])
    for i in range (1,n+1):
        print (f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#Alphabet Rangoli 
import string 
def print_rangoli(size):
    # your code goes here
    alphabet = string.ascii_lowercase 
    L = []
    
    for i in range(size):
        s = "-".join(alphabet[size-1:i:-1] + alphabet[i:size])
        L.append(s.center(4*size-3,'-'))
        
    print ('\n'.join(L[:0:-1] + L))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

#Capitalize!
def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

#Merge the Tools!
def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        sub = string[i:i +k]
        
        result = "".join(dict.fromkeys(sub))
        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

#Introduction to Sets
def average(array):
    # your code goes here
     distinct_heights = set(array)
     mean = sum(distinct_heights) / len(distinct_heights)
     return round (mean, 3)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#
import math
import os
import random
import re
import sys

#Birthday Cake Candles
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
   # Write your code here
    tallest_candles = max(candles)
    return candles.count(tallest_candles)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

