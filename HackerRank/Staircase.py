"""
This is a staircase of size n=4:
   #
  ##
 ###
####
Its base and height are both equal to . It is drawn using # symbols and spaces. The last line is not preceded by any spaces.
Write a program that prints a staircase of size n.

Function Description:
Complete the staircase function in the editor below.
staircase has the following parameter(s):
int n: an integer
"""
def staircase(n):
    # Write your code here
    a= "#"
    b= " "        
    for i in range (1, n+1):
        print(f"{b*(n-i)}{a*i}")
