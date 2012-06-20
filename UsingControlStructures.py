#Q5
print""
theInput = raw_input("Enter an integer: ")
#Your code here
theInput = int(theInput)
if theInput%2 == 0:
    print "even"
else:
    print "odd"

print"--------------------------------------------------------------------------"

#Q6
print""
primaryschool_age=6
voting_age=18
presidential_age=40
retirement_age=60
personAge = input ("Enter an age:")
if personAge<primaryschool_age:
    print "too young"
elif personAge>=voting_age:
    print"Remember to vote"
    if personAge<presidential_age:
        print "you cant be president"
    elif personAge>=presidential_age:
        print "Vote for me"
        if personAge>=retirement_age:
            print "too old"

print"----------------------------------------------------------------------------------------------------------------"

#Q7
print""
i=40
while i>0:
    if i%3==0:
        print i
    i=i-1
print"---------------------------------------------------------------------------------------------------"
#Q8
print""
i=0
for i in range(6,30):
    if i%2!=0 and i%3!=0 and i%5!=0:
        print i
print"---------------------------------------------------------------------------------------------------------------------"
#Q9
print""
n=1
while n>0:
    if(79*n)%97==1:
        print n
        break
    n=n+1
