import pickle
from pprint import pprint
with open("pruned_m4_n4_k3.pickle", "rb") as target:
    table = pickle.load(target)


pprint(table.shape)
# pprint(table[:,:,1].T)
pprint(table[:,:,2].T)
# pprint(table[:,:,3].T)