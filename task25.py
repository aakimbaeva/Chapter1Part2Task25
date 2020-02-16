def find():
    sent = input('Enter string: ').split()
    return max(sent, key=len)
print(find())
