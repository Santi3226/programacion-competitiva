n = 4
arr = ["word", "localization", "internationalization", "pneumonoultramicroscopicsilicovolcanoconiosis"]
for i in range(n):
    word = arr[i]
    if(len(word)>10):
        word = word[0] + str(len(word)-2) + word[len(word)-1]
        print(word)
    else:
        print(word)