'''import re
str1="she sells sea shells at sea shore"
p1='sea'
rep='ocean'
ns=re.sub(p1,rep,str1,1)
print(ns)

  output:she sells ocean shells at sea shore'''

'''import re
p=r"[aeiou]"
if re.search(p,"clue"):
    print("matchy vowel")

output:matchy vowel'''

'''import re
p=r"[a,e,i,o,u]"
if re.search(p,"clue"):
    print("matchy consonants")

output:matchy consonants'''
