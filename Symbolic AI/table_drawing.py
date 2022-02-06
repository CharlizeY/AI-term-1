import pickle
import matplotlib.pyplot as plt
import numpy as np



# max_m = 6
# max_n = 6
# max_k = 3
######################################################### x-axis m graphs

# fig, axs = plt.subplots(max_k, max_n)
# fig.suptitle("(x-axis: m), (y-axis: average(over 16 samples) time taken to run minimax on empty board)", fontsize="x-large")
# for k in range(1, max_k+1): 
# 	if k==3:
# 		for n in range(1, 5):
# 			axis = axs[k-1,n-1]
# 			axis.set_title("n: " + str(n) + ", k: " + str(k))
# 			axis.scatter(range(1,len(table[:,n,k])), table[1:,n,k])
# 			axis.plot(range(1,len(table[:,n,k])), table[1:,n,k])
# 	else:
# 		for n in range(1, max_n+1):
# 			axis = axs[k-1,n-1]
# 			axis.set_title("n: " + str(n) + ", k: " + str(k))
# 			axis.scatter(range(1,len(table2[:,n,k])), table2[1:,n,k])
# 			axis.plot(range(1,len(table2[:,n,k])), table2[1:,n,k])

# plt.show()
# plt.savefig('m_443_time.png')

# fig, axs = plt.subplots(max_k, max_n)
# fig.suptitle("(x-axis: m), (y-axis: LOG OF average(over 16 samples) time taken to run minimax on empty board)", fontsize="x-large")
# for k in range(1, max_k+1):
# 	if k==3:
# 		for n in range(1, 5):
# 			axis = axs[k-1,n-1]
# 			axis.set_title("n: " + str(n) + ", k: " + str(k))
# 			axis.scatter(range(1,len(table[:,n,k])), np.log(table[1:,n,k]))
# 			axis.plot(range(1,len(table[:,n,k])), np.log(table[1:,n,k]))
# 	else:
# 		for n in range(1, max_n+1):
# 			axis = axs[k-1,n-1]
# 			axis.set_title("n: " + str(n) + ", k: " + str(k))
# 			axis.scatter(range(1,len(table2[:,n,k])), np.log(table2[1:,n,k]))
# 			axis.plot(range(1,len(table2[:,n,k])), np.log(table2[1:,n,k]))

# plt.show()
# plt.savefig('m_443_logtime.png')


######################################################## x-axis n graphs
# fig, axs = plt.subplots(max_k, max_m)
# fig.suptitle("(x-axis: n), (y-axis: average(over 16 samples) time taken to run minimax on empty board)", fontsize="x-large")
# for k in range(1, max_k+1): 
# 	for m in range(1, max_m+1):
# 		axis = axs[k-1,m-1]
# 		axis.set_title("m: " + str(m) + ", k: " + str(k))
# 		axis.scatter(range(1,len(table[m,:,k])), table[m,1:,k])
# 		axis.plot(range(1,len(table[m,:,k])), table[m,1:,k])
# plt.show()
# plt.savefig('n_443_time.png')

# fig, axs = plt.subplots(max_k, max_n)
# fig.suptitle("(x-axis: m), (y-axis: LOG OF average(over 16 samples) time taken to run minimax on empty board)", fontsize="x-large")
# for k in range(1, max_k+1): 
# 	for m in range(1, max_m+1):
# 		axis = axs[k-1,m-1]
# 		axis.set_title("m: " + str(m) + ", k: " + str(k))
# 		axis.scatter(range(1,len(table[m,:,k])), np.log(table[m,1:,k]))
# 		axis.plot(range(1,len(table[m,:,k])), np.log(table[m,1:,k]))
# plt.show()
# plt.savefig('n_443_logtime.png')


######################################################### x-axis k graphs
# fig, axs = plt.subplots(max_m, max_n)
# fig.suptitle("(x-axis: k), (y-axis: average(over 16 samples) time taken to run minimax on empty board)", fontsize="x-large")
# for m in range(1, max_m+1): 
# 	for n in range(1, max_n+1):
# 		axis = axs[m-1,n-1]
# 		axis.set_title("m: " + str(m) + ", n: " + str(n))
# 		axis.scatter(range(1,len(table[m,n,:])), table[m,n,1:])
# 		axis.plot(range(1,len(table[m,n,:])), table[m,n,1:])
# plt.show()
# plt.savefig('k_443_time.png')

# fig, axs = plt.subplots(max_m, max_n)
# fig.suptitle("(x-axis: k), (y-axis: LOG OF average(over 16 samples) time taken to run minimax on empty board)", fontsize="x-large")
# for m in range(1, max_m+1): 
# 	for n in range(1, max_n+1):
# 		axis = axs[m-1,n-1]
# 		axis.set_title("m: " + str(m) + ", n: " + str(n))
# 		axis.scatter(range(1,len(table[m,n,:])), np.log(table[m,n,1:]))
# 		axis.plot(range(1,len(table[m,n,:])), np.log(table[m,n,1:]))
# plt.show()
# plt.savefig('k_443_logtime.png')



####################################################### x-axis m*n graphs
# For drawing the K=1 and K=2 curve, we use the m6_n6_k2 pickle.
# For drawing the K=3 curve, we use the m4_n4_k3 pickle
def draw_mn_curve(table, k, log=False):
	max_m = table.shape[0]-1
	max_n = table.shape[1]-1

	# create m_n_values and time_values
	m_n_values = []
	time_values = []
	for m in range(1,max_m+1):
		for n in range(1,max_n+1):
			m_n_values.append((m,n))
			time_values.append(table[m,n,k])
	if log:
		time_values = np.log(time_values)

	# now sort the mn_values and time_values while maintaining pairwise matches
	m_n_values, time_values = zip(*sorted(zip(m_n_values, time_values), key=lambda x: x[0][0]*x[0][1]))

	# draw points
	for (m,n), t in zip(m_n_values, time_values):
		plt.annotate(f"({m},{n})", (m*n,t))

	# make new list
	mn_values = [m*n for (m,n) in m_n_values]

	assert len(mn_values)==len(time_values)

	plt.plot(mn_values, time_values, label=f"k={k}")
	if k==3:
		print(m_n_values)
		print(time_values)


def draw_mn_curve_m(table, k, log=False, color="b"):
	max_m = table.shape[0]-1
	max_n = table.shape[1]-1
	print("@@@@@")
	print(max_m, max_n)

	# draw dots
	for m in range(1,max_m+1):
		for n in range(1,max_n+1):
			if n==max_n:
				if log:
					plt.annotate(f"m={m}", (m*n,np.log(table[m,n,k])))
				else:
					plt.annotate(f"m={m}", (m*n,table[m,n,k]))

	for m in range(1,max_m+1):

		assert len(range(0, (max_n+1)*m, m)) == len(table[m,:,k])
		if log:
			plt.plot(range(0, (max_n+1)*m, m), np.log(table[m,:,k])/np.log(m), color=color, label=f"k={k}")
			# plt.plot(range(0, (max_n+1)*m, m), np.log(table[m,:,k]), color=color, label=f"k={k}")
		else:
			plt.plot(range(0, (max_n+1)*m, m), table[m,:,k], color=color, label=f"k={k}")


def draw_mn_curve_n(table, k, log=False, color="b"):
	max_m = table.shape[0]-1
	max_n = table.shape[1]-1
	print("@@@@@")
	print(max_m, max_n)

	# draw dots
	for m in range(1,max_m+1):
		for n in range(1,max_n+1):
			if m==max_m:
				if log:
					plt.annotate(f"n={n}", (m*n,np.log(table[m,n,k])))
					# plt.annotate(f"({m},{n})", (m*n,np.log(table[m,n,k])))
				else:
					plt.annotate(f"n={n}", (m*n,table[m,n,k]))
					# plt.annotate(f"({m},{n})", (m*n,table[m,n,k]))

	for n in range(1,max_n+1):

		assert len(range(0, (max_m+1)*n, n)) == len(table[:,n,k])
		if log:
			plt.plot(range(0, (max_m+1)*n, n), np.log(table[:,n,k])/np.log(np.array(range(0,max_m+1))), color=color, label=f"k={k}")
			# plt.plot(range(0, (max_m+1)*n, n), np.log(table[:,n,k]), color=color, label=f"k={k}")
		else:
			plt.plot(range(0, (max_m+1)*n, n), table[:,n,k], color=color, label=f"k={k}")



log=True

###################################################################################

# draw_mn_curve(table2, k=1, log=log)
# draw_mn_curve(table2, k=2, log=log)
# draw_mn_curve(table, k=3, log=log)
# plt.title("Within a single line, both m and n varies")
# plt.xlabel("m * n")
# plt.ylabel("time_to_run_minimax_on_empty_board")
# plt.legend()
# plt.show()

###################################################################################

# draw_mn_curve_m(table2, k=1, log=log, color="tab:blue")
# draw_mn_curve_m(table2, k=2, log=log, color="tab:orange")
# draw_mn_curve_m(table, k=3, log=log, color="tab:green")
# plt.legend()
# plt.title("Each line parametrized wrt n")
# plt.xlabel("m * n")
# plt.ylabel("time_to_run_minimax_on_empty_board")
# plt.show()

###################################################################################

# draw_mn_curve_n(table2, k=1, log=log, color="tab:blue")
# draw_mn_curve_n(table2, k=2, log=log, color="tab:orange")
# draw_mn_curve_n(table, k=3, log=log, color="tab:green")
# plt.legend()
# plt.title("Each line parametrized wrt m")
# plt.xlabel("m * n")
# plt.ylabel("log(time_to_run_minimax_on_empty_board)")
# plt.show()


###################################################################################

# change these directories into pruned/unpruned version as you wish
with open("unpruned_m4_n4_k3.pickle", "rb") as target:
    table = pickle.load(target)

with open("unpruned_m6_n6_k2.pickle", "rb") as target:
    table2 = pickle.load(target)


draw_mn_curve_m(table2, k=1, log=log, color="tab:blue")
draw_mn_curve_m(table2, k=2, log=log, color="tab:orange")
draw_mn_curve_m(table, k=3, log=log, color="tab:green")

draw_mn_curve_n(table2, k=1, log=log, color="tab:blue")
draw_mn_curve_n(table2, k=2, log=log, color="tab:orange")
draw_mn_curve_n(table, k=3, log=log, color="tab:green")
# plt.legend()
# plt.title("Within a single line, only m, or only n varies")
# plt.xlabel("m * n")
# plt.ylabel("log(time_to_run_minimax_on_empty_board)")
# plt.show()


# change these directories into pruned/unpruned version as you wish
with open("pruned_m4_n4_k3.pickle", "rb") as target:
    table = pickle.load(target)
with open("pruned_m6_n6_k2.pickle", "rb") as target:
    table2 = pickle.load(target)

draw_mn_curve_m(table2, k=1, log=log, color="cyan")
draw_mn_curve_m(table2, k=2, log=log, color="red")
draw_mn_curve_m(table, k=3, log=log, color="lime")

draw_mn_curve_n(table2, k=1, log=log, color="cyan")
draw_mn_curve_n(table2, k=2, log=log, color="red")
draw_mn_curve_n(table, k=3, log=log, color="lime")
# plt.legend()
plt.title("Each line parametrized wrt n or m")
plt.xlabel("m * n")
plt.ylabel("log(time_to_run_minimax_on_empty_board)")
plt.show()

# change these directories into pruned/unpruned version as you wish
with open("unpruned_count_m4_n4_k3.pickle", "rb") as target:
    table = pickle.load(target)

with open("unpruned_count_m6_n6_k2.pickle", "rb") as target:
    table2 = pickle.load(target)


draw_mn_curve_m(table2, k=1, log=log, color="tab:blue")
draw_mn_curve_m(table2, k=2, log=log, color="tab:orange")
draw_mn_curve_m(table, k=3, log=log, color="tab:green")

draw_mn_curve_n(table2, k=1, log=log, color="tab:blue")
draw_mn_curve_n(table2, k=2, log=log, color="tab:orange")
draw_mn_curve_n(table, k=3, log=log, color="tab:green")
# plt.legend()
# plt.title("Within a single line, only m, or only n varies")
# plt.xlabel("m * n")
# plt.ylabel("log(time_to_run_minimax_on_empty_board)")
# plt.show()


# change these directories into pruned/unpruned version as you wish
with open("pruned_count_m4_n4_k3.pickle", "rb") as target:
    table = pickle.load(target)
with open("pruned_count_m6_n6_k2.pickle", "rb") as target:
    table2 = pickle.load(target)

draw_mn_curve_m(table2, k=1, log=log, color="cyan")
draw_mn_curve_m(table2, k=2, log=log, color="red")
draw_mn_curve_m(table, k=3, log=log, color="lime")

draw_mn_curve_n(table2, k=1, log=log, color="cyan")
draw_mn_curve_n(table2, k=2, log=log, color="red")
draw_mn_curve_n(table, k=3, log=log, color="lime")
# plt.legend()
plt.title("Each line parametrized wrt n or m")
plt.xlabel("m * n")
plt.ylabel("log(time_to_run_minimax_on_empty_board)")
plt.show()