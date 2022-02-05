l=0
def move(numberOfDiscs,movingFrom,to,using):
    global l
    if numberOfDiscs == 1:
        l = l + 1
        print(l,'Moving disc 1 from ',movingFrom,' do ',to)
    else:
        move(numberOfDiscs-1,movingFrom,using,to)
        l = l +1
        print(l,'Moving disc',numberOfDiscs,'from ',movingFrom,' do ',to)
        move(numberOfDiscs-1,using,to,movingFrom)

move(3,'A','C','B')