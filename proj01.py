def palindrome (in_str):
    s=str("")
    for i,le in enumerate(in_str):
        if le.isalpha():
            #le.remove(" ")
            le.lower()
            s+=le
    if s[::-1]==s:
        return True
    else:
        return False
        
    #for l in in_str:
     #   l.remove(" ")
      #  if l.isdigit():
       #     continue
        #elif l.isalpha:
         #   l.lower()
        #if l [::-1]==l:
         #   return True
    #else:
        return False# palindrome function definition goes here

in_str = input("Enter a string: ")
print('"{:s}" is '.format(in_str),end='')
if not palindrome(in_str):
    print("not ", end = '')
print("a palindrome.")