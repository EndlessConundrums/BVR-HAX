alphabet = "abcdefghijklmnopqrstuvwxyz"
rot13bet = "nopqrstuvwxyzabcdefghijklm"
def encryptor(plaintext):
    cyphertext = []
    for i in plaintext:
        for j in range(len(alphabet)):
            if i == alphabet[j]:
                cyphertext.append(rot13bet[j])
                print("letter appended")
    return cyphertext


sample = "Hello world!"
temp = encryptor(sample)
cypherSample = "".join(temp)
print(temp)
print(cypherSample)