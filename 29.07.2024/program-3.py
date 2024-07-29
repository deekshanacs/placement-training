string = "Data Science"
freq = {} 
for char in string: 
   if char in freq: 
      freq[char] += 1
   else: 
      freq[char] = 1
print ("Per char frequency in '{}' is :\n {}".format(string, str(freq)))
