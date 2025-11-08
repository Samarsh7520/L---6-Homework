a = input("Enter a character:")
if len(a) > 1:
    print("Write only 1 character to check")
else:
    if (a >= 'a' and a <= 'z') or (a >= 'A' and a <= 'Z'):
        print(a + " is an alphabter")
    else:
        print(a + " is not an alphabet")