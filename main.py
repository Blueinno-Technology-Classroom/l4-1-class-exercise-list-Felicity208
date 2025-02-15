##################################################
'''
Q1: 
'''

# TODO: Write your code here
sentence = ["It", "was", "a", "stormy", "night"]
print(sentence)
##################################################
'''
Q2:
'''

# TODO: Write your code here
sentence.insert(3, "dark")
sentence.insert(4, "and")
print(sentence)
##################################################
'''
Q3:
'''

# TODO: Write your code here
sentence[1] = "IS"
print(sentence)
##################################################
'''
Q4:
'''

# TODO: Write your code here
#sentence.remove("a")
#sentence.remove("dark")
#sentence.remove("and")
removal = []
for word in sentence:
    if "a" in word:
        removal.append(word)
for word in removal:
    sentence.remove(word)

print(sentence)
##################################################
'''
Q5:
'''

# TODO: Write your code here
numberlist = []
for i in range(0, 20, 2):
    numberlist.append(i)
print(numberlist)
##################################################
'''
Q6:
'''

# TODO: Write your code here
def fill(list, integer):
    for i in range(len(list)):
        list[i] = integer
    print(list)


number = [1, 4, 28, 32, 29]
fill(number, 9)
    

##################################################
