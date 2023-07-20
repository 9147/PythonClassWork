'''
    20 july 2023
'''

movies=[['Monty Python ans the HOly Grail',1975],
        ['Cat on a Hot Tin Roof',1951],
        ['On the Waterfront',1954]]
import pickle
with open("movies.bin",'wb') as file:
    pickle.dump(movies,file)