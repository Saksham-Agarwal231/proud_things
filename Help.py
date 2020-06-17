from datetime import date
import requests
import random
print("         *Help System*        ")
print("\n\n")

lis = ["0. Exit","1. Calculator", "2. Age calculator", "3. Factorial", "4. Fibonacci Sequence", "5. Rock-Paper-Scissor"]
lis1 = ["6. Table", "7. Prime numbers between a range", "8. Prime number check", "9. A frustrating game", "10. Print sqrt of list of no. or a no."]
lis3 = ["11. A password generator", "12. A lucky ducky game", "13. Just a grid","14. Weather Forecast", "15. Quiz"]
lis2 = lis + lis1 + lis3

for n in lis2:
    print(n)

def no1(k):
    e = k.split()

    num = int(e[0])
    char = str(e[1])
    num1 = int(e[2])

    if char == "+":
        return num + num1

    elif char == "-":
        return num - num1

    elif char == "/":
        return num / num1

    elif char == "*":
        return num * num1

    elif char == "//":
        return num // num1

    elif char == "%":
        return num % num1

    else:
        return -1

def no2(k):

    lol_age = 100 - k
    year = int(date.today().year)
    if k > 100:
        return -1

    else:
        return year + lol_age

def no3(k):
    if k == 1:
            return 1
    else:
            return k * no3(k - 1)


def no4(k):
    if k <= 1:
        return 1
    else:
        return no4(k - 1) + no4(k - 2)


def no5():
    hello = "A"

    while hello != "w":
        x = int(input("Enter the choice of first person: "))
        y = int(input("Enter the choice of second person: "))

        if x == 1 and y == 2:
            print("Rock vs paper")
            print("Player 2 wins!!")

        elif x == 1 and y == 1:
            print("Rock vs Rock")
            print("It is  a tie")

        elif x == 1 and y == 3:
            print("Rock vs Scissor")
            print("Player 1 is the winner")

        elif x == 2 and y == 1:
            print("Paper vs Rock")
            print("Player 1 wins")

        elif x == 2 and y == 2:
            print("Paper vs Paper")
            print("It is a tie")

        elif x == 2 and y == 3:
            print("Paper vs Scissor")
            print("Player 2 wins")

        elif x == 3 and y == 1:
            print("Scissor vs Rock")
            print("Player 2 wins")

        elif x == 3 and y == 2:
            print("Scissor vs Paper")
            print("Player 1 wins")

        elif x == 3 and y == 3:
            print("Scissor vs Scissor")
            print("It is a tie")

        else:
            print("Invalid input")

        hello = input("\n\nIf don't want to exit type any letter!!Want to quit??Type w:")


def no6(k):
    alt = []

    for i in range(1, 11):
        alt.append(i * k)

    for nu in alt:
        print(nu)

def no7(low, high):


    for num in range(low, high):
        for i in range(2, num):
            if num % i == 0:
                break

        else:
            print(num)

def no8(hello1):
  for n in range(2, hello1):
    if hello1 % n == 0:
        print(hello1, " is not a prime no.")
        break

  else:
        print(hello1, "is a prime no. ")


def no9():
    yoyo = "e"
    while yoyo != "q":
        print("This game is very simple!!You have to move @ to the top of the road using wasd")

        print("|---------------------------------------------------------|")
        print("|                                                         |")
        print("|                                                 ________|")
        print("|                                    ____________|   |    |")
        print("|           ________________________|   |    |   |   |    |")
        print("|_@________|    |    |    |    |    |   |    |   |   |    |")
        print("|   |   |       |                                         |")
        print("|---------------------------------------------------------|")

        inp = input("Enter the sequence required here: ")
        som = len(inp)
        hello = []
        for n in range(0, som):
            hello.append(inp[n])

        print("\n\n\n")
        if hello == ["d", "d", "w", "d", "d", "d", "d", "d", "w", "d", "d", "d", "w", "d", "d"]:
            print("|---------------------------------------------------------|")
            print("|                                                         |")
            print("|                                                 _______@|")
            print("|                                    ____________|   |    |")
            print("|           ________________________|   |    |   |   |    |")
            print("|__________|    |    |    |    |    |   |    |   |   |    |")
            print("|   |   |       |                                         |")
            print("|---------------------------------------------------------|\n\n")

            print("Good you win")
            yoyo = "q"

        else:
            print("You lose")
            yoyo = input("Want to quit?Press q(If not press any key): ")

def no10(k):
    est = k.split()
    alt1 = []
    alt2 = []
    for ba in est:
        hell = int(ba)
        alt2.append(hell)
    for n in alt2:
        for k in range(1, n):
            if k * k == n:
                alt1.append(k)
    for no in alt1:
        print(no)

def no11():
    import random
    print("     **Password Generator**   ")
    print("\n\n")
    print("0. Exit")
    print("1. Print a new pass word for you")
    print("2. View older passwords")
    hellimba = 12

    while hellimba != 0:
        hellimba = int(input("\n\nEnter the number for the action: "))
        if hellimba == 1:
            y = int(input("\nEnter how long your password should be:"))
            alt = []
            lower_case = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                          't',
                          "u", "v", "w", "x", "y", "z", "_"]
            for n in range(y):
                x = random.randint(0, 9)
                if x >= 0 and x <= 2:
                    raman = random.randint(0, len(lower_case) - 1)
                    alt.append(lower_case[raman])

                elif x >= 3 and x <= 6:
                    raman = random.randint(0, 9)
                    alt.append(raman)

                else:
                    raman = random.randint(0, len(lower_case) - 1)
                    alt.append(lower_case[raman].capitalize())

            for n in range(len(alt)):
                alt[n] = str(alt[n])

            hello = "".join(alt)
            print("\n", hello)

            saved = open("saved.txt", "a")

            saved.write("The password is: ")
            saved.write(hello)
            saved.write("\n")
            saved.close()

        elif hellimba == 2:
            saved = open("saved.txt", "r")
            hell = saved.readlines()
            for n in hell:
                print(n)

def no12():
    print("\n\n *A guess game* ")
    print("\n")
    print("The rules are simple.. You just need to guess the word the computer's number between 0 and 9. ")
    print("You got three chances!!! Try to win..\n\n")

    mguess = random.randint(0, 9)
    dice = {1: "first", 2: "second", 3: "third"}
    for n in range(1, 4):
        print("Enter your ", dice[n], "guess here: ", end="")
        yguess = int(input())

        if yguess == mguess:
            print("\nKuddos!!!Your guess is right")
            break

        elif yguess > mguess:
            print("\nYour guess was too high!!")

        elif yguess < mguess:
            print("\nYour guess was too low!!")

        if n == 3:
            print("\nThe number was ", mguess)
def no13():
    print("\n\n")
    def loll(meme):
        x = " ---"
        y = "|   "

        for n in range(meme):
            memey = meme - 1
            memes = meme + 1
            if n != memes - 1:
                print(x * meme)
                print(y * memes)
            else:
                print(x * memey)

    hello = int(input("Enter a number for no. of columns and rows in the grid: "))

    loll(hello)

def no14():
    # http://api.openweathermap.org/data/2.5/weather?q={City name}&appid=1cf36b0da43246d8f85bb8cd5696a905
    api_address = "http://api.openweathermap.org/data/2.5/weather?q="
    city = input('Place Name :')
    iss = "&appid=1cf36b0da43246d8f85bb8cd5696a905"
    url = api_address + city + iss
    json_data = requests.get(url).json()
    coord_add = json_data["coord"]
    weather = json_data['weather']
    temprs = json_data['main']
    print(city, "'s longitudenal extend: ", coord_add["lon"])
    print(city, "'s latitudenal extend: ", coord_add["lat"])
    print(city, "'s weather: ", weather[0]['main'])
    print(city, "'s temperature: ", temprs['temp'])

def no15():
 class Quiz:

     ans = ["a", "b", "c", "c","b", "a", "d"]
     points = 0
    
     @classmethod
     def check(cls,ans, no):
        if ans == cls.ans[no - 1]:
            cls.points = cls.points + 1

     @classmethod
     def see(cls):
        return cls.points

 def q1():
    print("\n\nWhat is the colour of sky?")
    print("a = blue\nb = violet \nc = red \nd = Yellow  ")

 def q2():
    print("\n\nHarry Potter was written by which author?")
    print("a = J.R.R Tolkien ")
    print("b = J.K. Rowling")
    print("c = Sir Arthur Conan Doyle")
    print("d = Idk")

 def q3():
    print("\n\nWho was the actor of Pirates of Carribean?")
    print("a = Chris Hemsworth \nb = Leonardo Da Caprio \nc = Johnny Depp \nd = Robert Downy Jr.")

 def q4():
    print("\n\nIn which year was minecraft released?")
    print("a = 2003 \nb = 2006 \nc = 2009 \nd = 2013")

 def q5():
    print("\n\nHow is Narotu's one and only best friend?")
    print("a = Shikamaru \nb = Sasuke \nc = Kakashi sensei \nd = Sakura")

 def q6():
    print("\n\nWhat is now a global pandemic?")
    print("a = CoronaVirus \nb = Tuberculosis \nc = Chicken Pox \nd = online tests")

 def q7():
    print("\n\nWhose son is Percy in Percy Jackson?")
    print("a = Zeus \nb = Atlas \nc = Hedas \nd = Poseidon")
 for n in range(1,8):
    if n == 1:
        q1()
        ans = input("\nYour ans: ")
        Quiz.check(ans,n)
        
    elif n == 2:
        q2()
        ans = input("\nYour ans: ")
        Quiz.check(ans,n)

    elif n ==3:
        q3()
        ans = input("\nYour ans: ")
        Quiz.check(ans,n)

    elif n == 4:
        q4()
        ans = input("\nYour ans: ")
        Quiz.check(ans,n)

    elif n == 5:
        q5()
        ans = input("\nYour ans: ")
        Quiz.check(ans,n)

    elif n == 6:
        q6()
        ans = input("\nYour ans: ")
        Quiz.check(ans,n)

    elif n == 7:
        q7()
        ans = input("\nYour ans: ")
        Quiz.check(ans,n)


 print("\n\n\ndo you want to see your report card??")
 print("\n\n'y' for yes and 'n' for no")

 x = input("Type your reaction here: ")

 if x == "y":
    print("You scored {}/7 marks!!".format(Quiz.see()))

 elif x == "n":
    print("You are a coward, my friend!! ")

 else:
    print("Bruhh!! Wrong syntax, now you have to do the quiz again!!")
    
def no16():
    print("    1   2   3  ")
    print("   --- --- --- ")
    print("a |   |   |   |")
    print("   --- --- --- ")
    print("b |   |   |   |")
    print("   --- --- --- ")
    print("c |   |   |   |")
    print("   --- --- --- ")
    print("\n\n\n")

    class tic:
        XL = "X |"
        YL = "0 |"

        XB = "X "
        YB = "0 "

        a1 = ["  |", 0, 0]
        a2 = ["  |", 0, 0]
        a3 = [" ", 0, 0]
        b1 = ["  |", 0, 0]
        b2 = ["  |", 0, 0]
        b3 = [" ", 0, 0]
        c1 = ["  |", 0, 0]
        c2 = ["  |", 0, 0]
        c3 = [" ", 0, 0]

        line = "---------"

        @classmethod
        def check(cls, inp, n):
            if inp == "a1":
                if n % 2 == 0:
                    cls.a1[0] = cls.XL
                    cls.a1[1] = 1

                elif n % 2 != 0:
                    cls.a1[0] = cls.YL
                    cls.a1[2] = 1

            elif inp == "a2":
                if n % 2 == 0:
                    cls.a2[0] = cls.XL
                    cls.a2[1] = 1


                else:
                    cls.a2[0] = cls.YL
                    cls.a2[2] = 1


            elif inp == "a3":
                if n % 2 == 0:
                    cls.a3[0] = cls.XB
                    cls.a3[1] = 1

                else:
                    cls.a3[0] = cls.YB
                    cls.a3[2] = 1

            elif inp == "b1":
                if n % 2 == 0:
                    cls.b1[0] = cls.XL
                    cls.b1[1] = 1

                else:
                    cls.b1[0] = cls.YL
                    cls.b1[2] = 1

            elif inp == "b2":
                if n % 2 == 0:
                    cls.b2[0] = cls.XL
                    cls.b2[1] = 1

                else:
                    cls.b2[0] = cls.YL
                    cls.b2[2] = 1

            elif inp == "b3":
                if n % 2 == 0:
                    cls.b3[0] = cls.XB
                    cls.b3[1] = 1
                else:
                    cls.b3[0] = cls.YB
                    cls.b3[2] = 1

            elif inp == "c1":
                if n % 2 == 0:
                    cls.c1[0] = cls.XL
                    cls.c1[1] = 1

                else:
                    cls.c1[0] = cls.YL
                    cls.c1[2] = 1

            elif inp == "c2":
                if n % 2 == 0:
                    cls.c2[0] = cls.XL
                    cls.c2[1] = 1

                else:
                    cls.c2[0] = cls.YL
                    cls.c2[2] = 1

            elif inp == "c3":
                if n % 2 == 0:
                    cls.c3[0] = cls.XB
                    cls.c3[1] = 1

                else:
                    cls.c3[0] = cls.YB
                    cls.c3[2] = 1
            else:
                print("Write something correct!! Atleast for once in your life!Try again!! :( \n")
                if n % 2 == 0:
                      a = input("Player 1! Enter your try here: ")
                      tic.check(a, n)
                else:
                      a = input("Player 2! Enter your try here: ")
                      tic.check(a, n)
        @classmethod
        def show(cls):
            print(cls.a1[0], cls.a2[0], cls.a3[0])
            print(cls.line)
            print(cls.b1[0], cls.b2[0], cls.b3[0])
            print(cls.line)
            print(cls.c1[0], cls.c2[0], cls.c3[0])

            if cls.a1[1] + cls.a2[1] + cls.a3[1] == 3 or cls.b1[1] + cls.b2[1] + cls.b3[1] == 3 or cls.c1[1] + cls.c2[
                1] + cls.c3[1] == 3:
                print("You won!!")
                return 1

            elif cls.a1[1] + cls.b1[1] + cls.c1[1] == 3 or cls.a2[1] + cls.b2[1] + cls.c2[1] == 3 or cls.a3[1] + cls.b3[
                1] + cls.c3[1] == 3:
                print("You won!!")
                return 1

            elif cls.a1[1] + cls.b2[1] + cls.c3[1] == 3 or cls.a3[1] + cls.b2[1] + cls.c1[1] == 3:
                print("You won!!")
                return 1

            elif cls.a1[2] + cls.a2[2] + cls.a3[2] == 3 or cls.b1[2] + cls.b2[2] + cls.b3[2] == 3 or cls.c1[2] + cls.c2[
                2] + cls.c3[2] == 3:
                print("You won!!")
                return 1

            elif cls.a1[2] + cls.b1[2] + cls.c1[2] == 3 or cls.a2[2] + cls.b2[2] + cls.c2[2] == 3 or cls.a3[2] + cls.b3[
                2] + cls.c3[2] == 3:
                print("You won!!")
                return 1

            elif cls.a1[2] + cls.b2[2] + cls.c3[2] == 3 or cls.a3[2] + cls.b2[2] + cls.c1[2] == 3:
                print("You won!!")
                return 1

    def lol():
        if n % 2 == 0:
            a = input("Player 1! Enter your try here: ")
            tic.check(a, n)
            h = tic.show()
            return h


        elif n % 2 != 0:
            a = input("Player 2! Enter your try here: ")
            tic.check(a, n)
            h = tic.show()

        else:
            pass

    for n in range(9):
        h = 0
        h = lol()

        if h == 1:
            break


hekko = int(input("\n\nEnter the number for the thing that you want to do: "))
hemmo = "w"

while hekko != 0:
 if hekko == 1:
    k = input("\n\nEnter your equation here: ")
    print("Your answer is ", no1(k))

 elif hekko == 2:
    k = int(input("\n\nEnter your age here: "))
    print("You getting to be of 100 years in ", no2(k))

 elif hekko == 3:
    k = int(input("\n\nEnter a number here: "))
    print("The factorial is ", no3(k))

 elif hekko == 4:
    k = int(input("\n\nEnter the no. here: "))
    print("The fibonacci sequence is: ")
    for n in range(k):
        print(no4(n))

 elif hekko == 5:
     print("\n\n1. Rock")
     print("2. Paper")
     print("3. Scissor")
     no5()

 elif hekko == 6:
    k = int(input("\n\nEnter the number here: "))
    no6(k)

 elif hekko == 7:
    low = int(input("\n\nType a lower number for selection: "))
    high = int(input("Type a higher number for selection: "))
    no7(low,high)

 elif hekko == 8:
    hello1 = int(input("\n\nEnter a number here: "))
    no8(hello1)

 elif hekko == 9:
    no9()

 elif hekko == 10:
    k = input("Write the number(s) here seperated by a witespace: ")
    no10(k)

 elif hekko == 11:
     no11()

 elif hekko == 12:
     no12()

 elif hekko == 13:
     no13()

 elif hekko == 14:
     no14()

 elif hekko == 15:
     no15()


 else:
     print("Write a number between the range")






 if hekko != 0 :
     hekko = int(input("\n\nEnter the number for the thing that you want to do: "))
