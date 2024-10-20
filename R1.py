#reading input
word = input()
#assinging a empty vari for get the first character get_char = it contains output
get_char = ''
#iterating on each character using loop
for i in word:
    #checking the character each which is appearing exactly once in String
    if word.count(i) == 1:
        #here we get the value which is stores in get_char
        get_char = i
        #we need only first non repeating value so after we got the value breaking loop here
        break
#printinh the final output here
print(get_char)