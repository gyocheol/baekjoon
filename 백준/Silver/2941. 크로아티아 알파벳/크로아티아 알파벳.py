croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alphabet = input()

for i in croatia:
    alphabet = alphabet.replace(i, '*')
print(len(alphabet))