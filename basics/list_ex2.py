books =['Steelheart','Firefight','Osmosis','Calamity']

books.append('The Final Empire')
books.append('Atomic Habit')
books.append('You Can Win')
books.append('Three mistakes of the life')

print('idx\t|book')
for i,b in enumerate(books):
    print(f'{i}\t|{b}')

books[6] ='The well of Ascension' #update 
books[-1]='The Hero of Ages' 
books[2]='Legion'

print('idx\t|book')
for i,b in enumerate(books):
    print(f'{i}\t|{b}')

books.insert(3,'Legion:Skin Deep')
books. insert(5,'Elantris')

print('idx\t|book')
for i,b in enumerate(books):
    print(f'{i}\t|{b}')


books.remove('Steelheart')
books.remove('Legion')

print('idx\t|book')
for i,b in enumerate(books):
    print(f'{i}\t|{b}')
