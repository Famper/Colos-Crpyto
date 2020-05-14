import sys
import crypto_lib

if (sys.argv[1] == ""):
    print('Error: Wrong Argument')
    exit()
else:
    path = sys.argv[1]

make = str(sys.argv[2])

print('PATH: \"{path}\"'.format(path=path))

try:
    with open(path, 'r') as file:
        text = file.readlines()
except FileNotFoundError:
    print('Error: File Not Found')
    exit()

with open('output.txt', 'w') as file:
    for line in text:
        if (make == 'enc'):
            file.write(crypto_lib.Crypto_Encode(line))
        elif (make == 'dec'):
            file.write(crypto_lib.Crypto_Decode(line))
        else:
            print('Error: Wrong Argument')
            exit()
