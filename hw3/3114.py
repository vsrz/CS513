#!/usr/bin/python

disks = [1,0,1,0,1,0,1,0]
n = 8

holes = []

for e in range(0,n):
  if disks[e] == 0:
    holes.append(disks[e])
  else:
    holes.insert(0,disks[e])

print holes

