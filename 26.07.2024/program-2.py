st=str(input("Enter your password : "))
le=len(st)
if le>6 and le<16:
    lc=any(c.islower()for c in st)
    up=any(c.isupper()for c in st)
    di=any(c.isdigit()for c in st)
    sp=any(c in '@#$' for c in st)
    if lc and up and di and sp:
        print("Password is valid!")
    else:
        print("Password is not valid!")
else:
    print("Length should be between 7-15")
