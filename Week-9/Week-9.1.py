A sentence is a string of single-space separated words where each word consists only of lowercase letters.A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
Example 1:
Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]

a=input().split()
b=input().split()
c1,c2,l={},{},[]
for i in a:
    c1[i]=c1.get(i,0)+1
for j in b:
    c2[j]=c2.get(j,0)+1
for w,c in c1.items():
    if(c==1 and w not in b):
        l.append(w)
for w,c in c2.items():
    if(c==1 and w not in a):
        l.append(w)
print(*l)
