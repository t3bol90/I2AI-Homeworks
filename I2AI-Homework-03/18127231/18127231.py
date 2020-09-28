# python==3.7.4
# python-sat==0.1.6.dev3

import numpy as np
import itertools
import sys

from pysat.solvers import Glucose3

import os
import getopt


def readMat(path):
	f = open(path, 'rt')
	h, w = [int(x) for x in f.readline().strip().split('\t')]
	assert h > 0 and w > 0
	mat = - np.ones((h, w), dtype=np.int32)
	for ih in range(h):
		iw = 0
		for it in f.readline().strip().split('\t'):
			if it != '.':
				mat[ih][iw] = int(it)
			iw += 1
	f.close()
	return mat


def toCNF(mat, lvars):
	'''
		input: 	mat: the matrix of puzzle's map/grid.
			   	lvars: the matrix of labels in mat.
		output: pre :: list[l1,l2..],
				the CNF clauses, combined all of cell's clause in the map.

	'''
	height = len(mat)
	width = len(mat[0])
	pre = []
	for i in range(height):
		for j in range(width):
			# Get all the clauses then add to one CNF clause!
			clauses = getClauses(mat, i, j)
			if clauses[0]:  # Maybe null :)))
				for clause in clauses:
					pre.append(clause)
	return pre


def getClauses(mat, ih, iw):
	clauses = []
	adjacents = getAllAdj(mat, lvars, ih, iw)
	for it in itertools.combinations(adjacents, mat[ih, iw] + 1):
		tmp = []
		for v in it:
			tmp.append(-v)
		clauses.append(tmp)

	for it in itertools.combinations(adjacents, len(adjacents) - mat[ih, iw] + 1):
		tmp = []
		for v in it:
			tmp.append(v)
		clauses.append(tmp)
	return clauses


def getAllAdj(mat, lvars, ih, iw):
	res = []
	for i in [-1, 0, 1]:
		for j in [-1, 0, 1]:
			ii = i + ih
			jj = j + iw
			if validCell(ii, jj, mat.shape) and lvars[ii][jj] not in res:
				res.append(lvars[ii][jj])
	return res


def validCell(i, j, shape):
	return 0 <= i and i < shape[0] and 0 <= j and j < shape[1]


def initVars(mat):
	hh, ww = mat.shape
	lvars = [[i*ww+j+1 for j in range(ww)] for i in range(hh)]
	return lvars, hh*ww


def solveCNF(clauses):
	g = Glucose3()
	for it in clauses:
		g.add_clause(it)
	sol = g.solve()
	if sol:
		return True, g.get_model()
	return False, None


def main(argv):
	global mat, lvars
	infile = 'input.txt'  # sys.argv[1]
	outfile = 'output.txt'  # sys.argv[2]
	try:
		opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
	except getopt.GetoptError:
		print('main.py -i <input_file> -o <output_file>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('main.py -i <input_file> -o <output_file>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			infile = arg
		elif opt in ("-o", "--ofile"):
			outfile = arg
	mat = readMat(infile)
	lvars, num = initVars(mat)
	clauses = toCNF(mat, lvars)
	sol, res = solveCNF(clauses)

	if not sol:
		print('UNSAT')
		exit()

	with open(outfile, 'wt') as g:
		for ih in range(mat.shape[0]):
			for iw in range(mat.shape[1]):
				if lvars[ih][iw] in res:
					g.write('G')
				else:
					g.write('R')
				g.write('\t')
			g.write('\n')
	print('SAT')


if __name__ == "__main__":
    main(sys.argv[1:])
