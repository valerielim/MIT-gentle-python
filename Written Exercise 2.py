# Valerie Lim
# Date: Jan 17 2016
# Title: Written Exercises 2

##### Exercise 2.11 String operations

look = 'look at me!'
now = ' NOW'

print "1. look[:4]", "is", "look"
print "Correct answer:", look[:4]
print

print "2. look[-1]", "is", "!"
print "Correct answer:", look[-1]
print

print "3. look*2", "is", "Look at me! Look at me!"
print "Correct answer:", look*2
print

print "4. look[:-1] + now + look[-1]", "is", "look at me NOW!"
print "Correct answer:", look[:-1] + now + look[-1]
print

print "5. now[1]", "is", "N"
print "Correct answer:", now[1]
print

print "6. now[4]", "is", " error"
print "Correct answer:", "NA because there is no 4th letter of now"
print

print "7. look*2 + look[:-1] + now + look[-1]", "is", "Look at me! Look at me!! NOW look at me"
print "Correct answer:", look*2 + look[:-1] + now + look[-1]
print
print
print
print 

##### Exercise 2.12 List Operations

print "Qn. 1: Write code such that expected output is '3'."
a_list = [3, 5, 6, 12]
print a_list[0]
print

print "Qn. 2: Write code such that expected output is '12'."
a_list = [3, 5, 6, 12]
print a_list[-1]
print

print "Qn. 3: Write code such that expected output is '5, 6, 12'."
a_list = [3, 5, 6, 12]
print a_list[1:]
print

print "Qn. 4: Write code such that expected output is '3 5 6 12', on separate lines."
a_list = [3, 5, 6, 12]
print a_list[0]
print a_list[1]
print a_list[2]
print a_list[3]

print "Qn. 5: Write code such that expected output is '12, 6, 5, 3'."
a_list = [3, 5, 6, 12]
print list(reversed(a_list))
print

print "Qn. 6: Write code such that expected output is '[9, 15,18, 36]'."
a_list = [3, 5, 6, 12]
print [x*3 for x in a_list]
print


print "Qn. 7: Write code such that expected output is '[False False True True]'."
a_list = [3, 5, 6, 12]
print [x>=6 for x in a_list]
print


