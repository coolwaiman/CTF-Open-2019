#!/usr/bin/env python

user_submitted = raw_input("Enter Password: ")

verify_arr = [114, 18, 19, 241, 179, 20, 87, 144, 21, 29, 23, 53, 29, 245, 144, 22, 29, 84, 212]
user_arr = []
for char in user_submitted:
  user_arr.append( (((ord(char) << 5) | (ord(char) >> 3)) ^ 123) & 255 )

print user_arr

if (user_arr == verify_arr):
  print "Success"
else:
  print "Wrong"
