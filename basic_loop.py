# Print all integers from 0 to 150.
for i in range (0,151):
    print(i)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
def multiples_of_five(m):
    for i in range(1000):
        print(i*m)

multiples_of_five(5)

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo"
for i in range(1,101):
    if i%5 == 0:
        print("coding")
        if i % 10 == 0:
            print ("dojo")

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
result = 0
def odd_total(i):
    for i in range(0, 500001):
        if i % 2 != 0:
         result += i
print(result)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for i in range (2018,0,-4):
    print(i)

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)


def counter(lowNum, highNum, mult):
    for val in range(lowNum, highNum+1):
        if val % mult == 0:
            print(val)

counter(2, 9, 3)