import numpy as np
import cPickle as cp
import sys

results_file = sys.argv[1]

results = cp.load(open(results_file))

threshold = results['threshold']
checkpoints = results['checkpoints']

p_mat = results['precision']
re_mat = results['recall']
time_mat = results['time']

summary = []

count_th = 0
for th in threshold:
	count_checkpoint = 0
	for checkpoint in checkpoints:
		p = p_mat[count_th,count_checkpoint,-1]
		r = re_mat[count_th,count_checkpoint,-1]
		t = time_mat[count_th,count_checkpoint,-1]

		f1 = 2.0*p*r/(p+1)

		summary.append(np.array([p,r,f1,t,th,checkpoint]))
		
		count_checkpoint += 1
	
	count_th += 1

summary = np.array(summary)

print summary

arg_list = np.argsort(summary[:,2])

reverse_list = list(arg_list)

reverse_list =  np.array(reverse_list[::-1])

summary = summary[reverse_list,:]

print summary

