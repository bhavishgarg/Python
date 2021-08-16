#Remove X
"""
Given a string, compute recursively a new string where all 'x' chars have been removed.

Input format :
String S

Output format :
Modified String
"""
Sample Input 1 :
xaxb
Sample Output 1:
ab

Sample Input 2 :
abc
Sample Output 2:
abc

Sample Input 3 :
xx
Sample Output 3:

Solution :

def removeX(s,x):
    if len(s)==0:
        return s

    smallOutput=removeX(s[1:],x)

    if s[0]==x:
        return smallOutput

    else:
        return s[0]+smallOutput

s=input()
r=removeX(s,'x')
print(r)


#Remove Duplicates Recursively
"""
Given a string S, remove consecutive duplicates from it recursively.

Input Format :
String S

Output Format :
Output string
"""
Sample Input 1 :
aabccba
Sample Output 1 :
abcba

Sample Input 2 :
xxxyyyzwwzzz
Sample Output 2 :
xyzwz

Solution :

def removeDuplicate(s):

    if len(s)==0 or len(s)==1:
        return s

    if s[0]==s[1]:
        smallOutput=removeDuplicate(s[1:])
        return smallOutput

    else:
        smallOutput=removeDuplicate(s[1:])
        return s[0]+smallOutput

s=input()
r=removeDuplicate(s)
print(r)






#Tower Of Hanoi
"""
Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. 
The objective of the puzzle is to move all disks from source rod to destination rod using third rod (say auxiliary). 
The rules are :
1) Only one disk can be moved at a time.
2) A disk can be moved only if it is on the top of a rod.
3) No disk can be placed on the top of a smaller disk.
Print the steps required to move n disks from source rod to destination rod.
Source Rod is named as 'a', auxiliary rod as 'b' and destination rod as 'c'.

Input Format :
Integer n

Output Format :
Steps in different lines (in one line print source and destination rod name separated by space)
"""
Sample Input 1 :
2
Sample Output 1 :
a b
a c
b c

Sample Input 2 :
3
Sample Output 2 :
a c
a b
c b
a c
b a
b c
a c

Solution :

def tower(n,a,b,c):

    if n==0:
        return

    if n==1:
        print(a,c )
        return

    tower(n-1,a,c,b)

    print(a,c)

    tower(n-1,b,a,c)

n=int(input())
tower(n,"a","b","c")
