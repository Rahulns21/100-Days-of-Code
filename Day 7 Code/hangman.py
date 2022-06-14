import random
import hangman_art, hangman_words

word_list = hangman_words.word_list

chosen_word = random.choice(word_list)
display = []
end_game = False
word_length = len(chosen_word)
lives = 6

print(hangman_art.logo)

for _ in range(word_length):
    display+='_'
print(display)

while not end_game:
  guess = input('Guess a letter: ').lower()

  for position in range(word_length):
      letter = chosen_word[position]  
      if letter == guess:
          display[position] = letter
   
  if guess not in chosen_word:
      lives -= 1
      print(hangman_art.stages[lives])
      print(f'Letter {guess} not in word')
      if lives == 0:
          end_game = True  
          print('You lose')
          print(f'The solution is {chosen_word}')

  print(display)

  if '_' not in display:
      end_game = True
      print('You win!')