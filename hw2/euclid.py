#!/usr/bin/python

def GCD(a,b):
  if b > a:
    c = a
    a = b
    b = c
  while (b != 0):
    remainder = a % b
    a, b = b, remainder
    print "A: %d B: %d" % (a,b)
  return a

a = 1489184184
b = 1281845142

print GCD(b,a)
