# Homework 03: Logic Representation

Courses `CSC14003`: Intro to Artificial Intelligence
`18CLC6`, `FIT - HCMUS`.
`20/08/2020`

This is an INDIVIDUAL assignment:
-   `18127231`: Đoàn Đình Toàn (GitHub: [@t3bol90](https://github.com/t3bol90))

---

## Problem:

#### Problem 1. (3.0pts) For each English sentence below, write the FOL sentence that best expresses its intended meaning. Use Cat(x) for “x is a cat,” Mouse(x) for “x is a mouse,” and Chases(x, y) for “x chases y.”

1. Every cat chases every mouse.

    **Ans:** 
    $$
    \forall x \space \forall y \text{ Cat(x) $\and$ Mouse(y) } \implies \text{Chases(x, y)}
    $$
    
2. For every cat, there is a mouse that the cat chases.

    **Ans:**
    $$
    \forall x \space \exists y \space Cat(x) \implies Mouse(y) \and Chases(x,y)
    $$
    
3. There is a cat who chases every mouse.

    **Ans:**
    $$
    \exists x \space \forall y \space Cat(x) \and (Mouse(y) \implies Chases(x,y))
    $$
    
4. Some cat chases some mouse.

    **Ans:**
    $$
    \exist x \space \exists y \space \space Cat(x) \and \space Mouse(y) \and Chases(x,y)
    $$
    
5. There is a mouse that every cat chases.

    **Ans:**
    $$
    \exists x \space \forall y \space Mouse(x) \and (Cat(y) \implies Chases(y, x))
    $$
    
6. For every mouse, there is a cat who chases that mouse.

    **Ans:**
    $$
    \forall x \space \exists y \space Mouse(x) \implies Cat(y) \and Chases(y,x)
    $$
    

#### Problem 2. (2.0pts) Given a knowledge base as follows

$$
P \or Q, Q \rightarrow (R \and S), (P \or R) \rightarrow U \space (*)
$$

Check whether each of the following sentences is entailed by KB using PL-Resolution

**Solution:**
Extract from $(*)$, $KB$:

I. $P \or Q$

II. $Q \rightarrow (R \and S) \iff \neg Q \or (R \and S) \iff (\neg Q \or R) \and (\neg Q \or S)$

III. $(P\or R) \rightarrow U \iff (\neg P \and \neg R )\or U \iff (\neg P \or U) \and (\neg R \or U)$

**a)** $U$
So the proof of $KB \models \alpha, \space \alpha = U$
I will proof by contradiction, we show that $KB \and \neg U$ is unsatisfiable.:

1. $\neg U$, from our hypothesis.
2. $\neg R \or U$, from (II).
3. $\neg R$, combined from 1 and 2.
4. $\neg Q \or R$ , from (II).
5. $\neg Q$, combined from 4 and 3.
6. $P \or Q$, from (I).
7. $P$, from 6 and 5.
8. $\neg P \or U$, from (III).
9. $U$, from 8 and 7 (It's unsatisfiable). (**)

Proof by PL-Resolution:.![image-20200823095010767](/home/t3bol90/.config/Typora/typora-user-images/image-20200823095010767.png)

Because of (\*\*), and two clauses resolve to yield the empty clause, in which case KB entails $U$ so we can proof $KB \models U $.
**b)** $\neg  U$
So the proof of $KB \models \alpha, \space \alpha = \neg U$
We need to show that $KB \and U$ is not satisfiable:
By using PL-Resolution, there are no new clauses that can be added, in which case KB does not entail $\neg U$.

#### Problem 03. (5.0pts) Given a Puzzle game board as below (Figure 01-a)

![](https://i.imgur.com/X8Ccc9V.png)

Each cell in the board is assigned a number or a blank (dot cells). The player needs to fill all cells
in green or red color so that the number of green cells around a cell with a number (including
adjacent ones and itself) is exactly the number (Figure 01-b).

**a) (3.0 pts)** Assign a logical variable to each cell in which the cell is green if the variable is
True and red if False. Write CNF clauses to restrict the game rule above for the given cell
below. Justify your procedure.

![](https://i.imgur.com/0pCptD0.png)

(**b) (2.0 pts)** Implement a program using Python and Glucose3 solver (Python-SAT:
https://pypi.org/project/python-sat/0.1.1dev7/) to solve the game board in Figure 01-a.
• Input: **input.txt** (tab separated)

	-	First line: 2 integers as the matrix shape
	-	Rest line: a matrix of numbers and dots
• Output: **output.txt** (tab separated)
	-	a matrix of letters G and R (green/red cells)
• Source code: attached one file only, filename is formatted like [student_number].py*
                	E.g. 12345678.py

```python
# Example for Glucose3
from pysat.solvers import Glucose3
g = Glucose3()
g.add_clause([-1, 2])
g.add_clause([-2, 3])
print (g.solve())
#True
print (g.get_model())
#[-1, -2, -3]
```

**Solution:**

**a.**

There is $\binom{9}{2}$ ways to assign logical values to the the given cells. Assume that we assign values $True$ (green) to $a$ and $b$. So the rest need to be $False$.

The clause for this case:
$$
\big[(A \and B) \implies (\neg C \and \neg D \and \neg E \and \neg F \and \neg G \and \neg H \and \neg I)\big] \and \\\big[(\neg C \and \neg D \and \neg E \and \neg F \and \neg G \and \neg H \and \neg I) \implies [(A \and B)\big]
$$
Then, it's equal to:
$$
\big[(A \and B) \iff (\neg C \and \neg D \and \neg E \and \neg F \and \neg G \and \neg H \and \neg I)\big] (*)
$$
Because the term "assigning True values to cells" depend on "assigning False values to cells" and otherwise. So we need to keep the constraints on both terms.

So $(*)$ equals to:
$$
(\neg A \or \neg B \neg C) \and (\neg A \or \neg B \neg D) \and (\neg A \or \neg B \neg E) \and \\
(\neg A \or \neg B \neg F) \and (\neg A \or \neg B \neg G) \and (\neg A \or \neg B \neg H) \and (\neg A \or \neg B \neg I) \and \\
(A \or C \or D \or E \or F \or G\or H \or I)\and(B \or C \or D \or E \or F \or G\or H \or I)
$$
This is CNF clause from of this case.

In generality:

$\forall x,y \in P, \space (x\neq y).$ With $P$ is a set of cells in this problem.

$Q = \{x, y\} \text{ and } K = P\setminus Q$.

Call $p_i$ is clause  of a case in $\binom{9}{2}$ cases which $x_i, y_i$ is assign $True$ and the rest is $False$ or $\forall k \in K_i, k := False$.

So the CNF form for $p_i$ is:
$$
[\bigwedge_{k \in K_i}^{}(\neg x_i \or \neg y_i \or \neg k)] \and \big[[x_i\or (\bigvee_{k \in K_i}k)] \and [y_i \or (\bigvee_{k \in K_i}k))]\big]
$$
**b.**

I have done 2 things on the templates file to complete this homework:

1. Complete the `toCNF` function, by read `pysat` documentation many times and research on Google "what is this function return?", "what is SAT model?", "How can solve SAT problem?", "What is 2-SAT, 3-SAT problems? Are they NP problems?",... Then, I learn somethings new but I realize that I just need to complete this function:

    ```python
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
    			clauses = getClauses(mat,i,j) ## Get all the clauses then add to one CNF clause!
    			if clauses[0]: ## Maybe null :)))
    				for clause in clauses:
    					pre.append(clause)
    	return pre
    ```

    *Thanks for this assignment, it's really helpful for our next project.*

2. The input, output parser is not good enough, and I think you want to write a  arguments style. So, I modify it:

    ```python
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
    ```

![image-20200823154220022](/home/t3bol90/.config/Typora/typora-user-images/image-20200823154220022.png)

Now, it's so cool :))).