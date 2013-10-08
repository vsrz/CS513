#!/usr/bin/python

matches = 0
A = "CABAAXBYA"

for i in range(0,len(A)):
  if A[i] == "A":
    for j in range(i,len(A)):
      if A[j] == "B":
        matches += 1
print matches

matches = 0
prefixes = 0
A = "CABAAXBYA"
for i in range(0,len(A)):
  if A[i] == "A":
    prefixes += 1
  elif A[i] == "B":
    matches += prefixes
print matches
