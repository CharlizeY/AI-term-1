import numpy as np
import time
import matplotlib.pyplot as plt
import pickle
from unpruned import Game as Unpruned_Game
from pruned import Game as Pruned_Game
from pprint import pprint


def draw_mnk_time_table(Game, max_m, max_n, max_k):
	max_m=int(max_m)
	max_n=int(max_n)
	max_k=int(max_k)

	table = np.zeros((max_m+1,max_n+1, max_k+1))

	for k in range(1,max_k+1):
		for m in range(k,max_m+1):
			for n in range(k,max_n+1):
				print("m,n,k: ", m, n, k)

				game = Game(m,n,k)

				start_time = time.perf_counter()
				# find best actions for the initial empty board
				_, _ = game.max(state = game.current_state, print_stuff=True)
				end_time = time.perf_counter()

				table[m, n, k] = end_time - start_time
	return table


def draw_avg_time_table(Game, max_m, max_n, max_k, repeats=1):
	avg_table = np.zeros((repeats, max_m+1,max_n+1, max_k+1))

	for repeat in range(repeats):
		avg_table[repeat] = draw_mnk_time_table(Game, max_m, max_n, max_k)


	avg_table = np.mean(avg_table, axis=0)

	return avg_table


def draw_mnk_count_table(Game, max_m, max_n, max_k):
	max_m=int(max_m)
	max_n=int(max_n)
	max_k=int(max_k)

	table = np.zeros((max_m+1,max_n+1, max_k+1))

	for k in range(1,max_k+1):
		for m in range(k,max_m+1):
			for n in range(k,max_n+1):
				print("m,n,k: ", m, n, k)

				game = Game(m,n,k)

				# find best actions for the initial empty board
				_, _ = game.max(state = game.current_state, print_stuff=True)

				table[m, n, k] = game.count
	return table


# table = draw_avg_time_table(Pruned_Game, max_m=6, max_n=6, max_k=3, repeats=16)
# with open("pruned_m6_n6_k3.pickle", "wb") as target:
#     pickle.dump(table, target)

# table = draw_avg_time_table(Pruned_Game, max_m=4, max_n=4, max_k=3, repeats=16)
# with open("pruned_m4_n4_k3.pickle", "wb") as target:
	# pickle.dump(table, target)

count_table = draw_mnk_count_table(Pruned_Game, max_m=6, max_n=6, max_k=2)
with open("pruned_count_m6_n6_k2.pickle", "wb") as target:
	pickle.dump(count_table, target)

count_table = draw_mnk_count_table(Unpruned_Game, max_m=6, max_n=6, max_k=2)
with open("unpruned_count_m6_n6_k2.pickle", "wb") as target:
	pickle.dump(count_table, target)
