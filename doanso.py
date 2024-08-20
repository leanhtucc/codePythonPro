import random
the_number = random.randint(1,10)
print(the_number)
guess=int(input("Ban doan so tu 1 den 10: "))
if guess==the_number:
    print(guess,"Dung roi, ban thang")
while guess != the_number:
    if guess > the_number:
        print(guess,"Khong phai, so to qua.")
        guess=int(input(" ban doan lai di: "))
        if guess == the_number:
            print(guess, "Dung roi, ban thang")
            break
    if guess < the_number:
        print(guess,"Khong phai so be qua.")
        guess=int(input(" ban doan lai di: "))
        if guess == the_number:
            print(guess, "Dung roi, ban thang")
            break
