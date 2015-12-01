#!/usr/bin/env python

import sys

cul_out_hex = sys.argv[1]

if cul_out_hex[0] is "i":
    cul_out_hex = cul_out_hex[1:17]
else:
    cul_out_hex = cul_out_hex[:16]


man_code = int(cul_out_hex, 16)
man_code = bin(man_code)
man_code = str(man_code[2:])
man_code = man_code.zfill(64)

ret = ""

for i in range(0, 32):
    temp = man_code[2*i] + man_code[2*i+1]
    if temp == "01":
        ret += "0"
    elif temp == "10":
        ret += "1"  
    else:
        print("There is definitely something wrong here!")
        break

print("\nThe string to enter in your serial terminal is:")
print("is"+ret+"\n")

print("The id of your remote control is:")
print(ret[:26]+"\n")

print("The group flag is:")
print(ret[26]+"\n")

print("Your device was set to:")
print(ret[27]+"\n")

print("The group code is:")
print(ret[28:]+"\n")
