import pickle
f = open('user.dat', 'rb')
a = pickle.load(f)
print(a)