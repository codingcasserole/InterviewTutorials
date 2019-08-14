from anagrams import anagram_solver

print("testing function for words: cat & cattle")
result=anagram_solver("cat", "cattle")
if result == False:
    print("your function returned: "+ str(result)+"   pass \n")
else:
    print("your function returned: "+ str(result)+"   fail \n")
print("testing function for words: cat & catt")
result=anagram_solver("cat", "catt")
if result == False:
    print("your function returned: "+ str(result)+"   pass\n")
else:
    print("your function returned: "+ str(result)+"   fail \n")
print("testing function for words: cat & \"\"")
result=anagram_solver("cat", "")
if result == False:
    print("your function returned: "+ str(result)+"   pass\n")
else:
    print("your function returned: "+ str(result)+"   fail \n")
print("testing function for words: listen & silent")
result=anagram_solver("listen", "silent")
if result == True:
    print("your function returned: "+ str(result)+"   pass\n")
else:
    print("your function returned: "+ str(result)+"   fail \n")
print("testing function for words: Dormitory & dirtyroom")
result=anagram_solver("Dormitory", "dirty room")
if result == False:
    print("your function returned: "+ str(result)+"   pass\n")
else:
    print("your function returned: "+ str(result)+"   fail \n")


