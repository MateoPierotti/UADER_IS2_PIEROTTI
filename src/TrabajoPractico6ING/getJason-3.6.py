# uncompyle6 version 3.9.1
# Python bytecode version base 3.6 (3379)
# Decompiled from: Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: getJason.py
# Compiled at: 2022-06-14 16:15:55
# Size of source mod 2**32: 214 bytes
import json, sys
jsonfile = sys.argv[1]
jsonkey = sys.argv[2]
with open(jsonfile, "r") as myfile:
    data = myfile.read()
obj = json.loads(data)
print(str(obj[jsonkey]))
