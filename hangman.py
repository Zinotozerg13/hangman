import random
logo = ''' 
 _                                             
| |                                            
| |__   _ _ _ _   _ _ _ _
_   _ _ _ _  
| '_ \ / _ | '_ \ / _ | '_  _ \ / _ | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''



stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print(logo)
end_of_game = False
word_list = ["mobile", "nepal", "sachin","computer","engineering","civil","hangman"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives=6
replay=''
display = []
for _ in range(word_length):
    display += "_"
print(display)


while not end_of_game:
   
    guess = input("Guess a letter: ").lower()
  
    if guess in display:
      print("U have already guessed the number")
      c=input("plz guess another alphabet")
      guess=c
     
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            lives=lives
            print("the word u guessed was correct")
            print(display)

  
    if guess not in chosen_word:
      print("u choose a wrong word")
      print(display)
      lives-=1
     
    print(stages[6-lives])
        
    print(f"u got {lives} chances left")
    if "_" not in display:
        end_of_game = True
        print("You won the game")
    elif lives==0:
      print("you lost the game")