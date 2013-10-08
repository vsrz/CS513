#/usr/bin/python
import sys

S = [[1,2],[2,4]]
L = []

# Adds the elements of a set into L
def addL(set,L):
  for each in set:
    L.append(each)
  return L
# L will contain a list of elements contained in the set
L = addL(S[0],[]) 

# Start the index at 1 since weve already added the first S
index = 1
while index < len(S):
  for element in S[index]:
    # If this element is found in L, then the
    # solution given is not disjoint
    for each in L:
      if element == each:
        print "False"
        sys.exit(0)
  L = addL(S[index],L)
  index += 1
print "True"
sys.exit(0)
