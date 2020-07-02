import pickle

word = 'app'

with open('word','wb') as file:
    pickle.dump(word,file)


with open('word','rb') as file:
    p = pickle.load(file)

print(p)