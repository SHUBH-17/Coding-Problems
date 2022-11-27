# given list: arr, Requirement : DRHPaoyoisapsecpyiynth
arr = ["Daisy","Rose","Hyacinth","Poppy"]

#Solution

#function which does the job but it requires length of the longest element 
#and input should be of string type and not a list type
charBuffer = []
def processWords(input,maxLen):
    s = input.split(" ")
    #below for loop was failing when the length of all strings were not equal (that's why appended dummy character '*')
    for i in range(0,maxLen):
        for values in s:
            #ignoring dummy symbol '*' 
            if values[i] == '*':
                continue
            else:
                charBuffer.append(values[i])
    return charBuffer

#storing length of the longest element of arr list
maxLength = len(max(arr, key=len))
# creating an empty list
myArr=[]
#appending all elements of arr into myArr and concatenating a dummy symbol '*' 
#in elements whose length < maxLength before appending it to myArr
for element in arr:
    if len(element) < maxLength:
        count = len(element)
        while count < maxLength:
            element += '*'
            count+=1
        myArr.append(element)
    else:
        myArr.append(element)

#converting list arr into string inputArr
inputArr = " ".join(map(str,myArr))

#passing string inputArr and maxLength to our function and storing it in result
result = processWords(inputArr,maxLength)

#print result
print(*result, sep = "")
