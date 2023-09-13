

"""
1!=1*1
2!=2*1!->2*1
3!=3*2->3*2*1
•
•
10!=10*9*8*••••*1

formula_n*(n-1)!
"""


def fact_rec(n):
  if n==0 or n==11:
    return 1
  else:
    return n* fact_rec(n-1)

number=int(input("enter a value"))
res=fact_rec(number)

print("the factorial of {}is{}". format (number,res))
