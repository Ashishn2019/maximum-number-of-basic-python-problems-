
'''("Accept five words as input and print the sentence formed by these words after adding a space between consecutive words and a full stop at the end.")
#(a=str(input())
#b=str(input())
#c=str(input())
#d=str(input())
#e=str(input())
#stop="."
#print ( a , b , c , d , e + stop)
("Accept the date in DD-MM-YYYY format as input and print the year as output.")
#number=input()
#print(number[6:])
("Accept a sequence of five single digit numbers separated by commas as input. Print the product of all five numbers")
#num = input()
##d2 = int(num[2])
#d3 = int(num[4])
#d4 = int(num[6])
#d5 = int(num[8])
#dproduct = d1 * d2 * d3 * d4 * d5
#print(dproduct)
("Assume that several IITs start offering online degrees across multiple branches. The email-id of a student is defined as follows:")
("CS_BT_21_7412@student.onlinedegree.iitm.ac.in")
#emid = input()
#branch=emid[:2]
#degree=emid[3:5]
#year=emid[6:8]
#institute=emid[-10:-6]
#print(branch)
#print(degree)
#print(year)
#print(institute)
#week 1 : 5("accept")
#x=int(input())
#y=int(input())
#print(x**y)'''
'''Accept a positive integer n as input and print the sum of the first  n terms of the series given below:
    1+ (1+2)+ (1+2+3)+ (1+2+3+4) ..........'''
'''n=int(input())
total=0
for i in range (1, n+1):
    for j in range (1 ,i+1):
        total=total+j
print(total)''' 
''' Accept a positive integer n, with n>1 as input from the user and print all the prime factors of n in ascending order.
n=int(input())
for i in range (2,n+1):
    if n % i == 0:
        is_prime = True
    for f in range (2 ,i):
        if i % f == 0:
            is_prime = False
            break
        if is_prime:
            print(i)'''
'''def  calculate_manhattan_distance(moves):
    x=0
    y=0
    for move in moves:
        if move=="up":
            y=+1
        if move=="down":
            y=-1
        if move=="left":
            x=-1
        if move=="right":
            x=+1
        distance=abs(x)+abs(y)
        return distance
moves=[]
while True:
    move=input()
    if move=="STOP":
        break
    moves.append(move)
distance=calculate_manhattan_distance(moves)
print(distance)'''
'''Accept a string as input, convert it to lower case, sort the string in alphabetical order, 
and print the sorted string to the console. You can assume that the string will only contain letters.
str= input()
str1= str.lower()
sorted_string= ''.join(sorted(str1))
print(sorted_string)'''
'''Accept a phone number as input. A valid phone number should satisfy the following constraints.

(1) The number should start with one of these digits: 6, 7, 8, 9

(2) The number should be exactly 10 digits long.

(3) No digit should appear more than 7 times in the number.

(4) No digit should appear more than 5 times in a row in the number.

If the fourth condition is not very clear, then consider this example: the number 9888888765 is invalid because the digit 8 appears more than 5 times in a row.

Print the string valid if the phone number is valid. If not, print the string invalid.
n=input()
valid=True
if len(n) == 10 and n[0]== 6 or 7 or 8 or 9 :
    for digit_index in range(0,5):
        count=n.count(n[digit_index])
        if count>7:
            valid=False
            break
        if 6* n [digit_index] in n:
            valid= False
            break
else:
    valid= False
if valid:
    print("valid")
else:
    print("invalid") '''
#In the first line of input, accept a sequence of space-separated words.
#In the second line of input, accept a single word. If this word is not present in the sequence, print NO.
#If this word is present in the sequence, then print YES and in the next line of the output, print the number of times the word appears in the sequence.
'''words=input().split(' ')
test=input()
if test not in words:
    print("NO")
else:
    print("YES")
    count=0
    for word in words:
        if test==word:
            count=+1
    print(count)'''
'''n=int(input())
A=[]
for i in range (n):
    row=[]
    for x in input().split(','):
        row.append(int(x))
    A.append(row)
B=[]
for i in range (n):
    row=[]
    for x in input().split(','):
        row.append(int(x))
    B.append(row)
C=[]
for i in range (n):
    row=[]
    for x in input().split(','):
        row.append(0)
    C.append(row)
for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][k]*B[k][j]
            if j!=n-1:
                print(C[i][j],end=',')
            else:
                print(C[i][j])'''
'''n = int(input())

# Accept matrix A
A = [ ]
for i in range(n):
    row = [ ]
    for x in input().split(','):
        row.append(int(x))
    A.append(row)

# Accept matrix B    
B = [ ]
for i in range(n):
    row = [ ]
    for x in input().split(','):
        row.append(int(x))
    B.append(row)

# Initialize matrix C as a zero-matrix
C = [ ]
for i in range(n):
    row = [ ]
    for j in range(n):
        row.append(0)
    C.append(row)

# Matrix product
for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]
        if j != n - 1:
            print(C[i][j], end = ',')
        else:
            print(C[i][j])'''
#The range of a list of numbers is the difference between the maximum and minimum values in the list.
#Write a function named get_range that accepts a list of real numbers as argument. It should return the range of the list.  
'''def get_max(L):
    maxi=L[0]
    for x in L:
        if x > maxi:
            maxi = x
    return maxi
def get_min(L):
    mini=L[0]
    for x in L:
        if mini>x:
            mini=x
    return mini
def get_range(L):
    maxi= get_max(L)
    mini= get_min(L)
    return maxi-mini
# get the maximum
def get_max(L):
    maxi = L[0]
    for x in L:
        if x > maxi:
            maxi = x
    return maxi

# get the minimum
def get_min(L):
    mini = L[0]
    for x in L:
        if x < mini:
            mini = x
    return mini

#get the range
def get_range(L):
    maxi = get_max(L)
    mini = get_min(L)
    return maxi - mini'''
    
def is_perfect(n):
    f_sum=0
    for i in range (1,n):
        if n % i==0:
            f_sum=+i
    return f_sum == n
print(is_perfect(int(input))
word_1=str(input())
word_2=str(input())
def distance (word_1,word_2):
    if len(word_1!=word_2):
        return -1
    letters= 'abcdefghijklmnopqrstuvwxyz'
    size=len(word_1)
    dist=0
    for i in range(size):
        c_1,c_2=word_1[i],word_2[i]
        d=abs(letters.index(c_1)-letters.index(c_2))
        dist =+ d
    return dist
        

             
               
    
    

            


                
    
    
    
    
    
    
    
    
    
    
   
    
    