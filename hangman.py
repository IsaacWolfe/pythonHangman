#!/usr/bin/python

import random

#Defines wordbanks for each category
animals = ("bee", "deer", "alligator", "fish", "bass", "rainbow trout", "bear", "crocodile", "zebra", "antelope", "snake", "cobra", "seagull", "hummingbird", "eagle", "monkey")

movies = ("pans labyrinth", "inglorious bastards", "baby driver", "pulp fiction", "star wars", "mrs doubtfire", "jumanjii", "forest gump")

tv = ("bobs burgers", "the flash", "rick and morty", "the simpsons", "family guy", "american dad", "stranger things", "ozark", "the office")

books = ("white fang", "the hobbit", "lord of the rings", "alice in wonderland", "tom sawyer", "moby dick")

artist = ("pink floyd", "childish gambino", "the beatles", "alice in chains", "jimi hendrix", "nickleback", "linkin park", "kendrick lamar", "frank ocean", "the who", "mozart", "migos", "credence clearwater revival", "america", "zac brown band", "cole swindel", "johnny cash", "three doors down", "daughtery", "adele")

#Defines the variables needed for the loop of playing again
playAgain = True
playAgainRound = 0

#Function that is called whenever the user is prompted if they want to play again or not
def playAgainFunc():
    choice = input("\nDo you want to play again? Enter y or n.\n")
    choice = choice.lower()
    if choice == 'y':
        playAgain = True
        return playAgain 
    elif choice == 'n':
        playAgain = False
        exit()
    else:
        print("Please enter a valid input")
        playAgainFunc()

#While loop that makes the program replay as long as the user chooses 
while playAgain:
    #Basic menu for selecting how to navigate the game
    menu = input("Select from the categories below or type exit to quit:\n1. Animals\n2. Movies\n3. TV Shows\n4. Books\n5. Singers/Bands\n6. Add New Word\n7. Remove Words\n")
    
    #Section resets variables so nothing is saved on loop
    word = ''
    guess = ''
    guess = guess.lower()
    wordBank = ''
    
    #playAgainUsed is variable used to make sure that playAgainFunc breaks to the right loop
    playAgainUsed = False
    if menu == "1":
        word = random.choice(animals)
        # word = "t e s"                                    #Test value
        #Removes white space of word
        wordStripped = word.replace(" ","")
        lenWord = len(wordStripped)
        correct = 0
        print("This word is ",lenWord,"letters long")
        blanks = len(word) * ["_"]
        #Used to put spaces back into the word
        if len(word) != lenWord:
            guess = " "
            if guess in word:
                for z, y in enumerate(word):
                    if y is guess:
                        blanks[z] = guess
        print(blanks)
        if lenWord <= 9:
            #Amount of turns if word is 9 or less characters
            turn = int(10)
            wordBank = ''
            print ("You have ",turn,"turns\n")
            while turn > 0:
                #Used to tell program to break to the right loop when playAgainFunc is used 
                if playAgainUsed == True:
                    playAgainUsed = False
                    break
                guess = input("Guess a letter\n")
                #guess = guess.lower()                      #Not working correctly 
                if guess in wordBank:
                    print("This has already been entered guess again.")
                    continue
                wordBank = wordBank + guess
                #print(wordBank)                            #Test value
                #Fills in the blanks if the guesses are in the word
                if guess in word:
                    correct += 1
                    for i, x in enumerate(word):
                        if x is guess:
                            blanks[i] = guess
                            print(blanks)
                        if "_" not in blanks:
                            print("Congratulations!")
                            playAgainFunc()
                            playAgainUsed = True
                            break
                #If the guess isnt in word subtracts a turn and prints turns left
                elif guess not in word:
                    turn -= 1
                    print("You have ",turn,"turns left")
            #Occurs if turns reach zero, playAgainFunc breaks to always the right point here
            if turn == 0:
                print("You lost\nThe word was",word)
                playAgainFunc()
                playAgainUsed = True
        elif lenWord > 10:
            #Amount of turns if the word is 10 characters or longer
            turn = int(15)
            wordBank = ''
            print ("You have ",turn,"turns\n")
            while turn > 0:
                #Used to tell program to break to the right loop when playAgainFunc is used 
                if playAgainUsed == True:
                    playAgainUsed = False
                    break
                guess = input("Guess a letter\n")
                #guess = guess.lower()                      #Not working correctly
                if guess in wordBank:
                    print("This has already been entered guess again.")
                    continue
                wordBank = wordBank + guess
                #print(wordBank)                            #Test value
                #Fills in the blanks if the guesses are in the word
                if guess in word:
                    correct += 1
                    for i, x in enumerate(word):
                        if x is guess:
                            blanks[i] = guess
                            print(blanks)
                        if "_" not in blanks:
                            print("Congratulations!")
                            playAgainFunc()
                            playAgainUsed = True
                            break
                #If the guess isnt in word subtracts a turn and prints turns left
                elif guess not in word:
                    turn -= 1
                    print("You have ",turn,"turns left")
            #Occurs if turns reach zero, playAgainFunc breaks to always the right point here
            if turn == 0:
                print("You lost\nThe word was",word)
                playAgainFunc()
                playAgainUsed = True

    elif menu == "2":
        word = random.choice(movies)
        # word = "t e s"                                    #Test value
        #Removes white space of word
        wordStripped = word.replace(" ","")
        lenWord = len(wordStripped)
        correct = 0
        print("This word is ",lenWord,"letters long")
        blanks = len(word) * ["_"]
        #Used to put spaces back into the word
        if len(word) != lenWord:
            guess = " "
            if guess in word:
                for z, y in enumerate(word):
                    if y is guess:
                        blanks[z] = guess
        print(blanks)
        if lenWord <= 9:
            #Amount of turns if word is 9 or less characters
            turn = int(10)
            wordBank = ''
            print ("You have ",turn,"turns\n")
            while turn > 0:
                #Used to tell program to break to the right loop when playAgainFunc is used 
                if playAgainUsed == True:
                    playAgainUsed = False
                    break
                guess = input("Guess a letter\n")
                #guess = guess.lower()                      #Not working correctly 
                if guess in wordBank:
                    print("This has already been entered guess again.")
                    continue
                wordBank = wordBank + guess
                #print(wordBank)                            #Test value
                #Fills in the blanks if the guesses are in the word
                if guess in word:
                    correct += 1
                    for i, x in enumerate(word):
                        if x is guess:
                            blanks[i] = guess
                            print(blanks)
                        if "_" not in blanks:
                            print("Congratulations!")
                            playAgainFunc()
                            playAgainUsed = True
                            break
                #If the guess isnt in word subtracts a turn and prints turns left
                elif guess not in word:
                    turn -= 1
                    print("You have ",turn,"turns left")
            #Occurs if turns reach zero, playAgainFunc breaks to always the right point here
            if turn == 0:
                print("You lost\nThe word was",word)
                playAgainFunc()
                playAgainUsed = True
        elif lenWord > 10:
            #Amount of turns if the word is 10 characters or longer
            turn = int(15)
            wordBank = ''
            print ("You have ",turn,"turns\n")
            while turn > 0:
                #Used to tell program to break to the right loop when playAgainFunc is used 
                if playAgainUsed == True:
                    playAgainUsed = False
                    break
                guess = input("Guess a letter\n")
                #guess = guess.lower()                      #Not working correctly
                if guess in wordBank:
                    print("This has already been entered guess again.")
                    continue
                wordBank = wordBank + guess
                #print(wordBank)                            #Test value
                #Fills in the blanks if the guesses are in the word
                if guess in word:
                    correct += 1
                    for i, x in enumerate(word):
                        if x is guess:
                            blanks[i] = guess
                            print(blanks)
                        if "_" not in blanks:
                            print("Congratulations!")
                            playAgainFunc()
                            playAgainUsed = True
                            break
                #If the guess isnt in word subtracts a turn and prints turns left
                elif guess not in word:
                    turn -= 1
                    print("You have ",turn,"turns left")
            #Occurs if turns reach zero, playAgainFunc breaks to always the right point here
            if turn == 0:
                print("You lost\nThe word was",word)
                playAgainFunc()
                playAgainUsed = True
 
    elif menu == "3":
        word = random.choice(tv)
        # word = "t e s"                                    #Test value
        #Removes white space of word
        wordStripped = word.replace(" ","")
        lenWord = len(wordStripped)
        correct = 0
        print("This word is ",lenWord,"letters long")
        blanks = len(word) * ["_"]
        #Used to put spaces back into the word
        if len(word) != lenWord:
            guess = " "
            if guess in word:
                for z, y in enumerate(word):
                    if y is guess:
                        blanks[z] = guess
        print(blanks)
        if lenWord <= 9:
            #Amount of turns if word is 9 or less characters
            turn = int(10)
            wordBank = ''
            print ("You have ",turn,"turns\n")
            while turn > 0:
                #Used to tell program to break to the right loop when playAgainFunc is used 
                if playAgainUsed == True:
                    playAgainUsed = False
                    break
                guess = input("Guess a letter\n")
                #guess = guess.lower()                      #Not working correctly 
                if guess in wordBank:
                    print("This has already been entered guess again.")
                    continue
                wordBank = wordBank + guess
                #print(wordBank)                            #Test value
                #Fills in the blanks if the guesses are in the word
                if guess in word:
                    correct += 1
                    for i, x in enumerate(word):
                        if x is guess:
                            blanks[i] = guess
                            print(blanks)
                        if "_" not in blanks:
                            print("Congratulations!")
                            playAgainFunc()
                            playAgainUsed = True
                            break
                #If the guess isnt in word subtracts a turn and prints turns left
                elif guess not in word:
                    turn -= 1
                    print("You have ",turn,"turns left")
            #Occurs if turns reach zero, playAgainFunc breaks to always the right point here
            if turn == 0:
                print("You lost\nThe word was",word)
                playAgainFunc()
                playAgainUsed = True
        elif lenWord > 10:
            #Amount of turns if the word is 10 characters or longer
            turn = int(15)
            wordBank = ''
            print ("You have ",turn,"turns\n")
            while turn > 0:
                #Used to tell program to break to the right loop when playAgainFunc is used 
                if playAgainUsed == True:
                    playAgainUsed = False
                    break
                guess = input("Guess a letter\n")
                #guess = guess.lower()                      #Not working correctly
                if guess in wordBank:
                    print("This has already been entered guess again.")
                    continue
                wordBank = wordBank + guess
                #print(wordBank)                            #Test value
                #Fills in the blanks if the guesses are in the word
                if guess in word:
                    correct += 1
                    for i, x in enumerate(word):
                        if x is guess:
                            blanks[i] = guess
                            print(blanks)
                        if "_" not in blanks:
                            print("Congratulations!")
                            playAgainFunc()
                            playAgainUsed = True
                            break
                #If the guess isnt in word subtracts a turn and prints turns left
                elif guess not in word:
                    turn -= 1
                    print("You have ",turn,"turns left")
            #Occurs if turns reach zero, playAgainFunc breaks to always the right point here
            if turn == 0:
                print("You lost\nThe word was",word)
                playAgainFunc()
                playAgainUsed = True
 
    elif menu == "4":
        word = random.choice(books)
        # word = "t e s"                                    #Test value
        #Removes white space of word
        wordStripped = word.replace(" ","")
        lenWord = len(wordStripped)
        correct = 0
        print("This word is ",lenWord,"letters long")
        blanks = len(word) * ["_"]
        #Used to put spaces back into the word
        if len(word) != lenWord:
            guess = " "
            if guess in word:
                for z, y in enumerate(word):
                    if y is guess:
                        blanks[z] = guess
        print(blanks)
        if lenWord <= 9:
            #Amount of turns if word is 9 or less characters
            turn = int(10)
            wordBank = ''
            print ("You have ",turn,"turns\n")
            while turn > 0:
                #Used to tell program to break to the right loop when playAgainFunc is used 
                if playAgainUsed == True:
                    playAgainUsed = False
                    break
                guess = input("Guess a letter\n")
                #guess = guess.lower()                      #Not working correctly 
                if guess in wordBank:
                    print("This has already been entered guess again.")
                    continue
                wordBank = wordBank + guess
                #print(wordBank)                            #Test value
                #Fills in the blanks if the guesses are in the word
                if guess in word:
                    correct += 1
                    for i, x in enumerate(word):
                        if x is guess:
                            blanks[i] = guess
                            print(blanks)
                        if "_" not in blanks:
                            print("Congratulations!")
                            playAgainFunc()
                            playAgainUsed = True
                            break
                #If the guess isnt in word subtracts a turn and prints turns left
                elif guess not in word:
                    turn -= 1
                    print("You have ",turn,"turns left")
            #Occurs if turns reach zero, playAgainFunc breaks to always the right point here
            if turn == 0:
                print("You lost\nThe word was",word)
                playAgainFunc()
                playAgainUsed = True
        elif lenWord > 10:
            #Amount of turns if the word is 10 characters or longer
            turn = int(15)
            wordBank = ''
            print ("You have ",turn,"turns\n")
            while turn > 0:
                #Used to tell program to break to the right loop when playAgainFunc is used 
                if playAgainUsed == True:
                    playAgainUsed = False
                    break
                guess = input("Guess a letter\n")
                #guess = guess.lower()                      #Not working correctly
                if guess in wordBank:
                    print("This has already been entered guess again.")
                    continue
                wordBank = wordBank + guess
                #print(wordBank)                            #Test value
                #Fills in the blanks if the guesses are in the word
                if guess in word:
                    correct += 1
                    for i, x in enumerate(word):
                        if x is guess:
                            blanks[i] = guess
                            print(blanks)
                        if "_" not in blanks:
                            print("Congratulations!")
                            playAgainFunc()
                            playAgainUsed = True
                            break
                #If the guess isnt in word subtracts a turn and prints turns left
                elif guess not in word:
                    turn -= 1
                    print("You have ",turn,"turns left")
            #Occurs if turns reach zero, playAgainFunc breaks to always the right point here
            if turn == 0:
                print("You lost\nThe word was",word)
                playAgainFunc()
                playAgainUsed = True
 
    elif menu == "5":
        word = random.choice(artist)
        # word = "t e s"                                    #Test value
        #Removes white space of word
        wordStripped = word.replace(" ","")
        lenWord = len(wordStripped)
        correct = 0
        print("This word is ",lenWord,"letters long")
        blanks = len(word) * ["_"]
        #Used to put spaces back into the word
        if len(word) != lenWord:
            guess = " "
            if guess in word:
                for z, y in enumerate(word):
                    if y is guess:
                        blanks[z] = guess
        print(blanks)
        if lenWord <= 9:
            #Amount of turns if word is 9 or less characters
            turn = int(10)
            wordBank = ''
            print ("You have ",turn,"turns\n")
            while turn > 0:
                #Used to tell program to break to the right loop when playAgainFunc is used 
                if playAgainUsed == True:
                    playAgainUsed = False
                    break
                guess = input("Guess a letter\n")
                #guess = guess.lower()                      #Not working correctly 
                if guess in wordBank:
                    print("This has already been entered guess again.")
                    continue
                wordBank = wordBank + guess
                #print(wordBank)                            #Test value
                #Fills in the blanks if the guesses are in the word
                if guess in word:
                    correct += 1
                    for i, x in enumerate(word):
                        if x is guess:
                            blanks[i] = guess
                            print(blanks)
                        if "_" not in blanks:
                            print("Congratulations!")
                            playAgainFunc()
                            playAgainUsed = True
                            break
                #If the guess isnt in word subtracts a turn and prints turns left
                elif guess not in word:
                    turn -= 1
                    print("You have ",turn,"turns left")
            #Occurs if turns reach zero, playAgainFunc breaks to always the right point here
            if turn == 0:
                print("You lost\nThe word was",word)
                playAgainFunc()
                playAgainUsed = True
        elif lenWord > 10:
            #Amount of turns if the word is 10 characters or longer
            turn = int(15)
            wordBank = ''
            print ("You have ",turn,"turns\n")
            while turn > 0:
                #Used to tell program to break to the right loop when playAgainFunc is used 
                if playAgainUsed == True:
                    playAgainUsed = False
                    break
                guess = input("Guess a letter\n")
                #guess = guess.lower()                      #Not working correctly
                if guess in wordBank:
                    print("This has already been entered guess again.")
                    continue
                wordBank = wordBank + guess
                #print(wordBank)                            #Test value
                #Fills in the blanks if the guesses are in the word
                if guess in word:
                    correct += 1
                    for i, x in enumerate(word):
                        if x is guess:
                            blanks[i] = guess
                            print(blanks)
                        if "_" not in blanks:
                            print("Congratulations!")
                            playAgainFunc()
                            playAgainUsed = True
                            break
                #If the guess isnt in word subtracts a turn and prints turns left
                elif guess not in word:
                    turn -= 1
                    print("You have ",turn,"turns left")
            #Occurs if turns reach zero, playAgainFunc breaks to always the right point here
            if turn == 0:
                print("You lost\nThe word was",word)
                playAgainFunc()
                playAgainUsed = True
 
#This section is to add new words as long as the user doesnt exit the program
    elif menu == '6':
        menu = input("What category would you like to add to?\n1. Animals\n2. Movies\n3. TV Shows\n4. Books\n5. Singers/Bands\n")
        addition = input("What word would you like to add?\n\tAdd terms that are at most two words.\n")
        addition = addition.lower()
        if menu == '1':
            animals = list(animals)
            animals.insert(0, addition)
            animals = tuple(animals)
            #print(animals)
        elif menu == '2':
            movies = list(movies)
            movies.insert(0,addition)
            movies = tuple(movies)
            #print(movies)
        elif menu == '3':
            tv = list(tv)
            tv.insert(0,addition)
            tv = tuple(tv)
        elif menu == '4':
            books = list(books)
            books.insert(0,addition)
            books = tuple(books)
        elif menu == '5':
            artist = list(artist)
            artist.insert(0,addition)
            artist = tuple(artist)
    
#Prints the list of whats in the category and removes whatever the user types
    elif menu == '7':
        menu = input("What category would you like to remove to?\n1. Animals\n2. Movies\n3. TV Shows\n4. Books\n5. Singers/Bands\n")
        if menu == '1':
            print(animals)
            remove = input("What word would you like to remove?\n")
            if remove in animals:
                animals = list(animals)
                animals.remove(remove)
                animals = tuple(animals)
            else:
                print("Please enter a valid input")
        #print(animals)
        
        elif menu == '2':
            print(movies)
            remove = input("What word would you like to remove?\n")
            if remove in movies:
                movies = list(movies)
                movies.remove(remove)
                movies = tuple(movies)
            else:
                print("Please enter a valid input")
                #print(movies)
                
        elif menu == '3':
            print(tv)
            remove = input("What word would you like to remove?\n")
            if remove in tv:
                tv = list(tv)
                tv.remove(remove)
                tv = tuple(tv)
            else:
                print("Please enter a valid input")

        elif menu == '4':
            print(books)
            remove = input("What word would you like to remove?\n")
            if remove in books:
                books = list(books)
                books.remove(remove)
                books = tuple(books)
            else:
                print("Please enter a valid input")

        elif menu == '5':
            print(artist)
            remove = input("What word would you like to remove?\n")
            if remove in artist:
                artist = list(artist)
                artist.remove(remove)
                artist = tuple(artist)
            else:
                print("Please enter a valid input")

#Exit section
    elif menu == "Exit" or menu == "exit":
        print("\nGoodbye")
        #Redundent
        playAgain = False
        exit()
    #This is so that y isn't taken as the input when trying to play again
    elif menu != 'y':
        print("Please enter a valid number on the menu\n")
