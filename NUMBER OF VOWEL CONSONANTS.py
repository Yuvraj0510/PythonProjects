word= str(input("ENTER WORD :"))
v = 0
c = 0
i = 0
while i<len(word):
  if word[i]=="a" or word[i]=="e" or word[i]=="i" or word[i]=="o" or word[i]=="u" or word[i]=="A" or word[i]=="E" or word[i]=="I" or word[i]=="O" or word[i]=="U" :
    v +=1
  elif word[i] == " " or word[i] == "." :
    print()
  else:
    c +=1
  i +=1
print ("\n", "NUMBER OF VOWELS=" ,v, "\n", "NUMBER OF CONSONANTS=", c)

    
        
