import random
import string

if __name__ == "__main__":
    p1 =string.ascii_letters
    p2 = string.digits
    p3 = string.punctuation

    lucky = int(input("Enter your password length::"))
    s = []
    s.extend(list(p1))
    s.extend(list(p2))
    s.extend(list(p3))
    

    random.shuffle(s)
    print("your password is :: \n")
    print("".join(s)[0:lucky])


