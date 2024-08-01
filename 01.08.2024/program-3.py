puncti = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str =str(inpit("Enter a string : "))
no_punct = ""
for char in my_str:
   if char not in puncti:
       no_punct = no_punct + char
print(no_punct)
