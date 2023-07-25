class Jinyng:

    def __init__(age, company, school):
        self.__age = age
        self.__school = school
        self.company = company

    def print():
        print(f"Hi, I'm jinyng.\n I'm {self.__age}"+
              f"I graduated from {self.__school}.\n"+
              f"I work for {self.company}")

    def setAge(age):
        self.__age = age
    def getAge():
        return self.__age

    def setSchool(school):
        return self.__school

if __name__ == "__main__":

    jinyng=Jinyng(25, "ChungBuk Univ.", "asd")

    jinyng.print()
