alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
rot13bet = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
extrabet = " .,?!:;<>'\""
def encryptor(plaintext):
    cyphertext = []
    for i in plaintext:
        for j in range(len(alphabet)):
            if i == alphabet[j]:
                cyphertext.append(rot13bet[j])
        for k in range(len(extrabet)):
            if i == extrabet[k]:
                cyphertext.append(extrabet[k])
    return cyphertext


sample = "Hello world!"
temp = encryptor(sample)
cypherSample = "".join(temp)
print(cypherSample)
temp = encryptor(cypherSample)
sample = "".join(temp)
print(sample)