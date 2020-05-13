import sys
import crypto_lib

i = 1
while (i < len(sys.argv)):
    text = crypto_lib.Crypto_Encode(sys.argv[i])
    crypto_lib.Crypto_Decode(text)
    i += 1
