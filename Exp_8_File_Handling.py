
with open("sample.txt", "r") as file:
    contents = file.read()
    words = contents.split()
    print("Number of words:", len(words))
