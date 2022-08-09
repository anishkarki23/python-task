class human:
    def __init__(self, name, eat, read, play):
        self.__name = name
        self.__eat = eat
        self.__read = read
        self.__play = play

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setEat(self, eat):
        self.__eat = eat

    def getEat(self):
        return self.__eat

    def setRead(self, read):
        self.__read = read

    def getRead(self):
        return self.__read

    def setPlay(self, play):
        self.__play = play

    def getPlay(self):
        return self.__play


class male(human):
    pass


m1 = male("anish", "momo", "Blog", "basketball")


m1.setName("jenny")
name = m1.getName()

m1.setEat("Chowmein")
eat = m1.getEat()

m1.setRead("Hobbits")
read = m1.getRead()

m1.setPlay("Football")
play = m1.getPlay()

print("Her name is ", name, "she likes to eat ", eat , "she likes to read", read, "and She loves to play ", play)
