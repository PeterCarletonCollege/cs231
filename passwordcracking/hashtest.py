#!/usr/bin/env python3
import hashlib
import binascii

# Compute the MD5 hash of this example password
password = 'moose' # type=string
print('password ({0}): {1}'.format(type(password), password))

encodedPassword = password.encode('utf-8') # type=bytes
print('encodedPassword ({0}): {1}'.format(type(encodedPassword), encodedPassword))

md5 = hashlib.md5(encodedPassword)
passwordHash = md5.digest() # type=bytes
print('passwordHash ({0}): {1}'.format(type(passwordHash), passwordHash))

passwordHashAsHex = binascii.hexlify(passwordHash) # weirdly, still type=bytes
print('passwordHashAsHex ({0}): {1}'.format(type(passwordHashAsHex), passwordHashAsHex))

passwordHashAsHexString = passwordHashAsHex.decode('utf-8') # type=string
print('passwordHashAsHexString ({0}): {1}'.format(type(passwordHashAsHexString), passwordHashAsHexString))
