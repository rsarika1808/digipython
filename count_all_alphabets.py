from helper import read

data =read('pride_n_prejudice.txt')

from string import ascii_lowercase
for letter in ascii_lowercase:
    counter =data.count(letter)
    print(f'{letter}found {counter} times')

#wap to find the most occuring and its frequency
freq=0
freq_letter=''
for letter in ascii_lowercase:
    counter =data.count(letter)
    print(f'{letter}found{counter}times')
    if freq<counter:
     freq=counter#70510
    freq_letter=letter#e
print(f'most frequent letter is{freq_letter} occurs {freq} times')