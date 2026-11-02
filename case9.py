strings = ["aaabbc", "aaaaaa", "abc", "bbbbbcc", "aabb"]

for i in range(5):
    text = strings[i]
    compressed = ""
    count = 1

    for j in range(len(text)):
        if j < len(text) - 1 and text[j] == text[j + 1]:
            count += 1
        else:
            compressed = compressed + text[j] + str(count)
            count = 1

    print("Test Case:", i + 1)
    print("Original String:", text)
    print("Compressed String:", compressed)

    if len(compressed) < len(text):
        print("Compression is Beneficial")
    else:
        print("Compression is Not Beneficial")