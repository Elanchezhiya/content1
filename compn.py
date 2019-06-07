o = int(input())
if o > 1:
    for i in range(2, o):
        if (o % i) == 0:
            print("yes")
            break
    else:
        print("no")
