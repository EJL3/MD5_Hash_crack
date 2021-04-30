import hashlib
flag = 0

pass_hash = input('Enter hashed password =>')
wordlist = input('Enter password wordlist =>')
wordlist = open(wordlist, 'r')

for word in wordlist:
    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest() # can change hash algorithm (hashlib.select type)

    if digest == pass_hash:
        print('Password found!!')
        print('Password is:-' + word)
        flag = 1
        break
if flag == 0:
    print('Password is not in the list' )
