'''
AP CREATE TASK REQS - 9 hr class time
30% ap score

1) must create and call a function that takes and uses a parameter
    a) inside
        - must use loop
        - must trigger selection statement SOMETIMES
    b) anywhere
        - use a list


'''
alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
]
def encryptIt(phrase, shift):
    #location to store our new letter
    new_phrase_list = []

    #cycle through each incoming letter 
    for char in phrase.lower():
        #check if the letter is in our alphabet
        if char in alphabet:
            #find the index of that letter
            current_index = alphabet.index(char)
            #print(current_index)
            #calculate shift based on parameter
            new_index = current_index + shift
            #handle jumping past z
            if new_index >= len(alphabet):
                new_index = new_index - len(alphabet)
            #storing new letter in new phrase list
            new_phrase_list.append(alphabet[new_index])
        else:
            new_phrase_list.append(char)
    #print(new_phrase_list)
    #convert list back to list item into a single string
    newphraseword = ''.join(new_phrase_list)
    print("\n"+phrase+" turned into: "+newphraseword)

incomingphrase = input("Enter a phrase to encrypt: ")
incomingshift = int(input("Enter a shift number (1-25):")) 
encryptIt(incomingphrase, incomingshift)
#BLEH xD

