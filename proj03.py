''' Project 03
have alphabet and keys
for encripting make sure entered keyword is within guidelines
add letters into empty string
affine with equation
for decription
rebuild keys and compare message to each key'''

answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ")

while answer.upper() != 'Q': #given
    
    
    alphabet = "abcdefghijklmnopqrstuvwxyz" #beginning
    ckey = "" #caesar key
    akey = "" #affine key
    a, b, m = 5, 8, 26
    if answer == "E": #encript
        keyword = input("Please enter a keyword: ")
        keywordl = keyword.lower()
        if keyword.isalpha() and len(keyword) <= 26:
            
            for letter in keywordl:
                if letter not in ckey:
                    ckey += letter # adds letter from keyword into ckey minus any repeats
            for lette in alphabet:
                if lette not in ckey:
                    ckey += lette # adds the rest of the alphabet
            #caesar key built
            
            
            #this affine key
            for ch in ckey: #for each letter in ckey
                x = ckey.find(ch) #alphabet.index(ch) #find the index of each character
                toaffine = ckey[(a*x+b)%(m)] #do math and find it in ckey
                akey += toaffine
                #affine key built
            
            message = input(str("Enter your message: ")) #encodes message
            lowmessage = message.lower()
            encmessage = ""
            for let in lowmessage:
                if let.isalpha():
                    enc = akey[alphabet.find(let)]#finds each letter that matches alphabet
                    encmessage += enc # adds the letter to encoded message
                else:
                    encmessage += let #adds spaces and punctuation to the encoded message
                    
            print("your encoded message: ", encmessage)
            
        else: 
            print("There is an error in the keyword. It must be all letters and a maximum length of 26")
            continue
            
            
            
    if answer == "D": #decript
        
        key = input("Please enter a keyword: ")
        nkey = "" #new key
        message2 = input(str("Enter your message: "))
        if keyword.isalpha() and len(keyword) <= 26:
            
            for i in key:#recreate key similar to how ckey was made
                if i not in nkey:
                    nkey += i # adds letter from keyword into nkey minus any repeats
            for i in alphabet:
                if i not in nkey:
                    nkey += i
            
        new_alphabet = ""  #new alphabet    
        for i in range(len(nkey)):
            new_alphabet += nkey[(a*i+b)%26] #affine key
        
        plaintext = "" #decoded message
        for c in message2:
            if c in nkey:
                plaintext += alphabet[new_alphabet.index(c)] #using index to build the new alphabet
            else:
                plaintext += c
                  

        print("your decoded message: ", plaintext)
        
    answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ") #given
    if answer == "Q":
        print("See you again soon!")