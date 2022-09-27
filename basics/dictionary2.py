movies ={}

movies['Top Gun:Maverick']=8.3
movies['Everything Everywhere All ar Once']=8.1
movies['Spider-Man: No WayHome']=8.2


for item in movies:
    print(item)

    print(' both key andvalues')
    for key in movies:
        print(key,movies[item])
        
print('using dict.items()method')
for k,v in movies.items():
    print(k,v)

#user input
for i in range(3):
    name =input('Movie Name:')
    rating =float(input('Movie Rating:'))
    movies[name] =rating
    
print('using dict.items()method')
for k,v in movies.items():
    print(k,v)
    