### Numpy Exercises
# Boolean Indexing
data_1 = data[label == 1].transpose()
data_2 = data[label == 2].T # two different ways of transpose a np.array

assert data_1 == np.array([[5.46, 7.28, 2.72, 6.05],
                           [3.06, 3.06, 3.11, 2.72]])

assert data_2 == np.array([[2.08, 3.35, 2.51, 3.91, 0.84, 1.14],
                           [1.57, 4.74, 2.43, 4.55, 3.57, 6.31]])


# Numpy functions
x = np.array([[18, 3, 9], [1, 30, 4], [7, 5, 23]])
distribution = x.sum(axis = 1)/x.sum()
# distribution = np.sum(x, axis=1) / np.sum(x)
assert all(distribution == np.array([0.3, 0.35, 0.35]))


x = np.array([[18, 3, 9], [1, 30, 4], [7, 5, 23]])
accuracy = x.diagonal().sum()/x.sum()
# accuracy = np.sum(np.diagonal(x))/np.sum(x)
assert accuracy == 0.71




