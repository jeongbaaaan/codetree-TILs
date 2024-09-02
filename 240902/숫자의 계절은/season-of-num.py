m = int(input())
if m >= 12 or m <= 2:
    print("Winter")
elif m <= 5 or m >= 3:
    print("Spring")
elif m <=8 or m >= 6:
    print("Summer")
else:
    print("Fall")