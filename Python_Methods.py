#Python String replace() Method
# syntax: string.replace(oldvalue, newvalue, count)
#count - Optional. A number specifying how many occurrences of the old value you want to replace. 
# Default is all occurrences

#1. Replace 1st g only with ch
string = 'geeksFORgeeks'
string = string.replace('g','ch',1)
print(string)

#2. Remove 1st two e from the string
string = 'geeksFORgeeks'
string = string.replace('e','',2)
print(string)

# Remove 4th index from the string
string = 'geeksFORgeeks'
string = string.replace(string[4],'',1)
print(string)


#------------------------------------------------------------------------------------------------------------#
