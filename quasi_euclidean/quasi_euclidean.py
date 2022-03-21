import numpy as np
import scipy.spatial

def bicenter_weighted(matrix):
	row_weights = np.ones((matrix.shape[0],1))
	col_weights = np.ones((1,matrix.shape[1]))
	row_weights /= row_weights.sum()
	col_weights /= col_weights.sum()
	row_mean = np.sum(matrix * row_weights, axis=0)
	col_mean = np.sum(matrix * col_weights, axis=1)
	col_mean -= np.sum(row_mean * col_weights)
	result = matrix - row_mean
	result -= col_mean.reshape(-1,1)
	return result

def quasi_euclidean(distance_matrix):
	num_cols = distance_matrix.shape[1]
	delta = -0.5 * bicenter_weighted(distance_matrix * distance_matrix)
	eigenvalues, eigenvectors = np.linalg.eigh(delta)
	num_components = np.count_nonzero(eigenvalues > 0)
	new_table = eigenvectors[:,-num_components:] * np.tile(np.sqrt(eigenvalues[-num_components:]), (num_cols, 1))
	result = scipy.spatial.distance_matrix(new_table, new_table)
	return result