''' Insert heading comments here.'''

answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ")

while answer.upper() != 'Q': #given
    
    
    alphabet = "abcdefghijklmnopqrstuvwxyz" #beginning
    ckey = ""
    akey = ""
    a, b, m = 5, 8, 26
    if answer == "E": #encript
        keyword = input ("Please enter a keyword: ")
        keywordl = keyword.lower()
        if keyword.isalpha() and len(keyword) <= 26:
            #print(keywordl)
            for letter in keywordl:
                if letter not in ckey:
                    ckey += letter # adds letter from keyword into ckey minus any repeats
            for lette in alphabet:
                if lette not in ckey:
                    ckey += lette # adds the rest of the alphabet
            print(ckey)
            
            Cmessage = input ("Enter your message: ")
            cipher = ""
            modmessage = Cmessage.lower
            #bad_chars = Cmessage.whitespace + Cmessage.digits + Cmessage.punctuation
            #cmessage = Cmessage.whitespace #dont know how to get rid of spaces and then put them back
            #print(cmessage)
            #for char in modmessage:
            #    if char in bad_chars:
            #        modmessage = modmessage.replace(char, ' ')
            for ch in modmessage:
                x = alphabet.index(ch) #find index of each character
                affine = ckey[(a*x+b)%(m)] #do math and find it in ckey
                cipher += affine
            print("your encoded message: ", affine) # print word
        else: 
            continue
                
                
    print("Testing:", answer) #given
    answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ") #given