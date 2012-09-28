import random;

# Rolls 1-50, and has user guess until they are correct.
def spinner():

        spin = random.randint(1,50);

        while(True):
            Target = input('Pick a number(1-50): ');
            if(Target > spin):
                print 'Too high';
            elif(Target < spin):
                print 'Too low';
            else:
                print 'Correct!!';
                again = raw_input("Would you like to play again?(Y/N) ");
                spin = random.randint(1,50);
                if(again == "n" or again == "N"):
                    break;
                    print "Good-Bye";

#Generates 2 Random coordinates, takes 2 input coordinates and checks if you
#guessed correctly. You have 20 Turns to guess correctly, enabling hints adds 15.
#Typing (99,99) tells you what the location is, but ends the game.
def HaS():

   x = random.randint(1,10);
   y = random.randint(1,10);
   turn = 0;
   hints = False;

   print 'I bet you can not find me in 20 turns!'
   print 'Type (50,50) to enable hints (costs 15 turns).';
   print 'Type (99,99) to get the location (ends the game).';

#Infinite loop that breaks when the user uses 20 guesses, cheats, or wins.
   while(True):
       xCoord = input('What is your X-Coordinate(1-10)? ');
       yCoord = input('What is your Y-Coordinate(1-10)? ');
       turn += 1;

#Prints hint statements.
       if(hints == True):
           if(xCoord > x):
               print 'X is too big';
           if(xCoord < x):
               print 'X is too small';
           if(yCoord > y):
               print 'Y is too big';
           if(yCoord < y):
               print 'Y is too small';

#Prints the coordinates, ends the game.
       if(xCoord == 99 and yCoord == 99):
           print 'X =',x,'Y =',y,'CHEATER!!';
           AgainHaS();
           break;

       if(xCoord == x and yCoord == y):
           print 'You found me!!';
           AgainHaS();
           break;
#Enables hints.
       elif(xCoord == 50 and yCoord == 50):
           hints = True;
           print 'Hints Enabled +15 turns.';
           turn += 14;
       else:
           print'Wrong spot';

#Gives the user a limited number of turns to guess in.
       if(turn >= 20):
           print 'Ok, I am in',x,',',y;
           AgainHaS();
           break;

#Algorithm for playing again.
def AgainHaS():

    again = raw_input("Would you like to play again?(Y/N) ");

    if(again == "y" or again == "Y"):
        HaS();
    elif(again == "n" or again == "N"):
        print "Good-bye";
    else:
        print "Your statement was not recognized, please re-enter your request";
        AgainHaS();
HaS();
