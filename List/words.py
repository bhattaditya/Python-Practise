word_string =  "The quick brown fox jumps over the lazy dog"
new_string_list = []

n = int(input(">: "))

for word in word_string.split(" "):
    if len(word) > n:
        new_string_list.append(word)

print(new_string_list)
