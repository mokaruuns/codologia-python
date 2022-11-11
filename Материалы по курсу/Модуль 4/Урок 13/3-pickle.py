import pickle

locations = {'Home': 'mine', 'Square': 'yours', 'River': 'ours'}

file = open("file.pickle", "wb")
pickle.dump(locations, file)
# pickle.load(locations)
file.close()
