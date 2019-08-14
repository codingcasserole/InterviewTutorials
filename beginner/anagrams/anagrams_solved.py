def anagram_solver(x, y):
    x=x.replace(" ","")
    y=y.replace(" ","")
    x=sorted(x)
    y=sorted(y)
    if x != y:
        return False
    else: 
        return True

#Really good blog post explaining the solutions (including the one faster then sort http://nafiulis.me/the-deceptive-anagram-question.html)
