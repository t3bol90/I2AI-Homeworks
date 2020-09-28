# **HOMEWORK** 04

Courses `CSC14003`: Intro to Artificial Intelligence
18CLC6, FIT - HCMUS.
`09/09/2020`

This is a team homework for 2 students, but for some reason - can not form a team, so I do it as
a individual assignment : 

-   `18127231`: Đoàn Đình Toàn (GitHub: [@t3bol90](https://github.com/t3bol90))

---
## Problem:
###  Problem 1. (3.0pts)
**A  robot  in  a  lumber yard   learns   to   discriminate   Oak   wood from  Pine  wood.  It  learns  a  decision  tree classifier from the examples shown aside:**

| ![image-20200908145408104](/home/t3bol90/.config/Typora/typora-user-images/image-20200908145408104.png) |
| :----------------------------------------------------------: |
|                        **Table 1.1**                         |

**a. (2.0pts) Build a decision tree using the ID3 Decision Tree Induction algorithm.**

**b. (1.0pt) Classify these new examples as Oak or Pine using the decision tree above.**

| **\[Density=Light, Grain=Small, Hardness=Hard\]** |
| :-----------------------------------------------: |
| **\[Density=Light, Grain=Small, Hardness=Soft\]** |

### Problem  2. (2.0pts)

**Consider  the  following  training  dataset,  in  which Transportationis  the target attribute. Show calculations to choose an attribute for the root node of the ID3 decision tree**

| ![image-20200908150334067](/home/t3bol90/.config/Typora/typora-user-images/image-20200908150334067.png) |
| :----------------------------------------------------------: |
|                        **Table 2.1**                         |

### Problem  3.(2.0pts):

**Consider  the  data  setshown aside.  A  and  B  are  numerical  attributes  and  Z  is  a Boolean classification**

| ![image-20200908150423359](/home/t3bol90/.config/Typora/typora-user-images/image-20200908150423359.png) |
| :----------------------------------------------------------: |
|                        **Table 3.1**                         |

**a. Let  P  be  the  perceptron  that  has  two  input  neurons  for  the two  atttributes,  A  and  B,  and one  bias  of  constant  value  1.  The  correponding  weights  are  `wA =  2`,  `wB=  1`,  and  `wo= -4.5` (for bias). What is the total error after training one epoch?**

**b. Provide your analysis to find a set of weights and a threshold that categorizes all this data correctly.**

### Problem  4.  (3.0pts):

**Given a neural network with two inputs, two hidden neurons, two output neurons, as shown below. Additionally, in the hidden and output layers, each of which will include a bias that has a constant output value of 1.**

![image-20200908150757351](/home/t3bol90/.config/Typora/typora-user-images/image-20200908150757351.png)

- **Learning rate 0.5**

- **Input values: i1=0.05 i2=0.10**

- **Target values: t1=0.01 t2=0.99**

- **Bias values: b1=0.35 b2=0.60**

- **Initial weight:**	

    | w1     | 0.15     |
    | ------ | -------- |
    | **w2** | **0.20** |
    | **w3** | **0.25** |
    | **w4** | **0.30** |
    | **w5** | **0.40** |
    | **w6** | **0.45** |
    | **w7** | **0.50** |
    | **w8** | **0.55** |

    **Present all calculations required to perform the backpropagation once (i.e. one forward pass and one backward pass) on the given neural network in the following cases**

    **a. Ignore all biases.**

    **b. Take into account all biases.**



## Answers:

### Problem 1:

#### a. 

With the Entropy formula:
$$
H(S) = \Sigma_{x \in X}  -p(x)\log_2 p(x)
$$
and the Information gain:
$$
  IG(S,A) = H(S) - \Sigma_{t\in T} p(t)H(t) = H(S) - H(S|A)
$$
`ID3` algorithms pseudo code[^(1)]:

```python
ID3 (Examples, Target_Attribute, Attributes)
    Create a root node for the tree
    If all examples are positive, Return the single-node tree Root, with label = +.
    If all examples are negative, Return the single-node tree Root, with label = -.
    If number of predicting attributes is empty, then Return the single node tree Root,
    with label = most common value of the target attribute in the examples.
    Otherwise Begin
        A ← The Attribute that best classifies examples.
        Decision Tree attribute for Root = A.
        For each possible value, vi, of A,
            Add a new tree branch below Root, corresponding to the test A = vi.
            Let Examples(vi) be the subset of examples that have the value vi for A
            If Examples(vi) is empty
                Then below this new branch add a leaf node with label = most common target value in the examples
            Else below this new branch add the subtree ID3 (Examples(vi), Target_Attribute, Attributes – {A})
    End
    Return Root
```

Then we  run ID3 algorithm on problem's data set:

In iteration-1:
$$
\newcommand{\t}[1]{\text{#1}}
H(S) = -p(\t{class = 'Oak'}) \times \log_2(p(\t{class = 'Oak'})) \\-p(\t{class = 'Pine'}) \times \log_2(p(\t{class = 'Pine'})) = 0.5 + 0.5 = 1
$$


| Features | IG(Features, S)                                     |
| -------- | --------------------------------------------------- |
| Density  | 1 - 0.5 - 0.5 = 0                                   |
| Grain    | 1 - 0.5 -0.5 = 0                                    |
| Hardness | 1 - 0.31127812445913283 - 0.5 = 0.18872187554086717 |

$\rightarrow$ Choose 'Hardness' as root.

Then split 'Hardness' out off data set.

![image-20200908171755318](/home/t3bol90/.config/Typora/typora-user-images/image-20200908171755318.png)

In iteration-2:
$$
\newcommand{\t}[1]{\text{#1}}
H(\t{Harness}) = 0.8112781244591328
$$
- Hard hardness on decision:
| Density | Grain | Hardness | Class |
|---------|-------|----------|-------|
| Heavy   | Small | Hard     | Oak   |
| Heavy   | Large | Hard     | Oak   |
| Heavy   | Small | Hard     | Oak   |
| Light   | Large | Hard     | Pine  |

| Features | IG(Features, Hardness)                         |
| -------- | ---------------------------------------------- |
| Density  | 0.8112781244591328 - 0.0 = 0.8112781244591328  |
| Grain    | 0.8112781244591328 - 0.5 = 0.31127812445913283 |

$\rightarrow$ choose Density as attribute.


- Soft hardness on decision:
| Density | Grain | Hardness | Class |
|---------|-------|----------|-------|
| Light   | Large | Soft     | Oak   |
| Heavy   | Small | Soft     | Pine  |
| Heavy   | Large | Soft     | Pine  |
| Heavy   | Small | Soft     | Pine  |

| Features | IG(Features, Hardness)                         |
| -------- | ---------------------------------------------- |
| Density  | 0.8112781244591328 - 0.0 = 0.8112781244591328  |
| Grain    | 0.8112781244591328 - 0.5 = 0.31127812445913283 |

$\rightarrow$ choose Density as attribute.

![image-20200908173858083](/home/t3bol90/.config/Typora/typora-user-images/image-20200908173858083.png)

At the end of iteration, we can predict the Class of tuple because there is no multiple result on each branch.

![image-20200908174640811](/home/t3bol90/.config/Typora/typora-user-images/image-20200908174640811.png)

Finish build `ID3 Decision Tree`.

#### b. 

|                   Examples                    | Result   |
| :-------------------------------------------: | -------- |
| \[Density=Light, Grain=Small, Hardness=Hard\] | **Pine** |
| \[Density=Light, Grain=Small, Hardness=Soft\] | **Oak**  |

### Problem 2:

We have this table from `Table 2.1`

| Gender | Car Ownership | Travel Cost | Income Level | Transportation |
| ------ | ------------- | ----------- | ------------ | -------------- |
| Male   | 0             | Cheap       | Low          | Bus            |
| Male   | 1             | Cheap       | Medium       | Bus            |
| Female | 1             | Cheap       | Medium       | Train          |
| Female | 0             | Cheap       | Low          | Bus            |
| Male   | 1             | Cheap       | Medium       | Bus            |
| Male   | 0             | Standard    | Medium       | Train          |
| Female | 1             | Standard    | Medium       | Train          |
| Female | 1             | Expensive   | High         | Car            |
| Male   | 2             | Expensive   | Medium       | Car            |
| Female | 2             | Expensive   | High         | Car            |

With 4 features: [Gender, Car Ownership, Income Level, Transportation] we can calculate Entropy and Information Gain in the table below:
$$
\newcommand{\t}[1]{\text{#1}}
H(S) = p(\t{Transportation = Train}) \times \log_2(p(\t{Transportation = Train})) \\ 
+ p(\t{Transportation = Bus}) \times \log_2(p(\t{Transportation = Bus})) \\
+ p(\t{Transportation = Car}) \times \log_2(p(\t{Transportation = Car})) \\
= 0.5210896782498619 + 0.5287712379549449 + 0.5210896782498619 = 1.5709505944546684
$$
**Splitting on Gender:**

- On Male Gender (`p=5/10 = 0.5`):
    $$
    \begin{aligned}
    
    p(\t{Transportation = Train}|\t{Gender = Male}) &= 1/5 = 0.2,\\
    \implies \log_2(p(\t{Transportation = Train}|\t{Gender = Male})) &= -2.321928094887362,
    \\ \implies p(\t{Transportation = Train}|\t{Gender = Male}) \times \log_2(p(\t{Transportation = Train}|\t{Gender = Male})) &= -0.46438561897747244 \\
    \end{aligned}
    $$


$$
\begin{aligned}

p(\t{Transportation = Bus}|\t{Gender = Male}) &= 3/5 = 0.6,\\
\iff \log_2(p(\t{Transportation = Bus}|\t{Gender = Male})) &= -0.7369655941662062,
\\ \iff p(\t{Transportation = Bus}|\t{Gender = Male}) \times \log_2(p(\t{Transportation = Bus}|\t{Gender = Male})) &= -0.44217935649972373 \\
\end{aligned}
$$

$$
\begin{aligned}

p(\t{Transportation = Car}|\t{Gender = Male}) &= 1/5 = 0.2,\\
\implies \log_2(p(\t{Transportation = Car}|\t{Gender = Male})) &= -2.321928094887362,
\\ \implies p(\t{Transportation = Car}|\t{Gender = Male}) \times \log_2(p(\t{Transportation = Car}|\t{Gender = Male})) &= -0.46438561897747244 \\
\end{aligned}
$$

$$
\implies H(S|Gender = Male) = 1.3709505944546687
$$

- On Female Gender (`p=5/10 = 0.5`):

    In the same way with these step above:
    $$
    \begin{aligned}
    p(\t{Transportation = Train}|\t{Gender = Female}) &\times \log_2(p(\t{Transportation = Train}|\t{Gender = Female})) &= &-0.5287712379549449\\
    p(\t{Transportation = Bus}|\t{Gender = Female}) &\times \log_2(p(\t{Transportation = Bus}|\t{Gender = Female}))  &= &-0.46438561897747244\\
    p(\t{Transportation = Car}|\t{Gender = Female}) &\times \log_2(p(\t{Transportation = Car}|\t{Gender = Female}))  &= &-0.5287712379549449\\
    \end{aligned}
    $$
    

$$
\implies H(S|Gender = Male) = 1.5219280948873621
$$

$$
\begin{aligned}
&\implies H(\t{S|Gender}) &=& 0.5*1.3709505944546687 + 0.5*1.5219280948873621 &=& 1.4464393446710155 \\
&\implies IG(\t{S,Gender}) &=& 1.5709505944546684 - 1.4464393446710155 &=& 0.12451124978365291
\end{aligned}
$$

**Splitting on Car Ownership:**
$$
\begin{aligned}
&\implies H(\t{S|Car OwnerShip}) &=& 1.036452797660028 \\
&\implies IG(\t{S,Car OwnerShip}) &=& 1.5709505944546684 - 1.036452797660028 = 0.5344977967946405
\end{aligned}
$$
**Splitting on Travel Cost:**
$$
\begin{aligned}
&\implies H(\t{S|Travel Cost}) &=& 0.36096404744368116 \\
&\implies IG(\t{S,Travel Cost}) &=& 1.5709505944546684 - 0.36096404744368116 = 1.2099865470109874
\end{aligned}
$$
**Splitting on Income Level:**
$$
\begin{aligned}
&\implies H(\t{S|Income Level}) &=& 0.8754887502163469 \\
&\implies IG(\t{S,Income Level}) &=& 1.5709505944546684 - 0.8754887502163469 = 0.6954618442383216
\end{aligned}
$$
The maximum `IG` attribute is `Travel Cost`, then is selected as splitting attribute aka root node of the `ID3` decision tree.

### Problem 3:

#### a.

In first epoch:
$$
a = hardlim(n)= hardlim(W_p + b)
$$
The `perceptron` output follow the rule that $a_i \geq 0$ will be `T` and $a_i < 0$ will label at `F`.

The error function for `perceptron` is `L1 error`:
$$
\text{L1}_\text{error} = \Sigma_{i=1}^{n}|y_\text{true} - y_\text{predict}|
$$




| A    | B    | Z    | a                        | e     |
| ---- | ---- | ---- | ------------------------ | ----- |
| 1    | 2    | T    | $2.1 + 1.2 - 4.5 = -0.5$ | $0.5$ |
| 2    | 1    | F    | $2.2 + 1.1 - 4.5 = 0.5$  | $0.5$ |
| 3    | 2    | T    | $3.2 + 2.1 - 4.5 = 2.5$  | $0$   |
| 1    | 1    | F    | $1.2 + 1.1 - 4.5 = -1.5$ | $0$   |

Total error in first epoch: $0.5 + 0.5 = 1$.

#### b.

After plot the data to graph:

![image-20200910162315644](/home/t3bol90/.config/Typora/typora-user-images/image-20200910162315644.png)

Our init weight:

![image-20200910162357904](/home/t3bol90/.config/Typora/typora-user-images/image-20200910162357904.png)

We need a better line which split data set into 2 clusters. Let start with $w_A = 0, w_b = 1, w_0 = -1.5$

![image-20200910162520689](/home/t3bol90/.config/Typora/typora-user-images/image-20200910162520689.png)

It's will easy to converge.

### Problem 4:

#### a.

**The forward pass:**


| ![image-20200911171604928](/home/t3bol90/.config/Typora/typora-user-images/image-20200911171604928.png) |
| :----------------------------------------------------------: |
|               **Neuron net: ignore all bias**                |
|                                                              |

| Variable | Value |
| -------- | ----- |
| $\t{h1}_\t{in} = \t{w1}.\t{i1} + \t{w2}.\t{i2}$ | $=$ $0.027500$ |
| $\t{h1}_\t{out} = \frac{1}{1+e^{-\t{h1}_\t{in}}} = \frac{1}{1+e^{-0.0275}}$ | $= 0.506875$ |
| $\t{h2}_\t{in} = \t{w3.i1 + w4.i2}$ | $=0.042500$ |
| $\t{h2}_\t{out}$ | $= 0.510623$   |
| $\t{o1}_\t{in} = \t{h1.w5 + h2.w6}$ | $= 0.432530$ |
| $\t{o1}_\t{out}$ | $= 0.606478$ |
| $\t{o2}_\t{in} = \t{h1.w7 + h2.w8}$ | $= 0.534280$ |
| $\t{o2}_\t{out}$ | $= 0.630481$ |



**Calculate total error:**
$$
\t{E}_\t{total} = (1/2) \Sigma (\t{target - output})^2
$$



| Variable          | Value        |
| ----------------- | ------------ |
| $\t{E}_\t{o1}$    | $= 0.177893$ |
| $\t{E}_\t{o2}$    | $= 0.064627$ |
| $\t{E}_\t{total}$ | $= 0.242163$ |

**The backward pass:**

- **Output layer:** $\newcommand{\px}{\partial}$

Using backward propagation of errors methods, to update $w_i$, we calculate $\frac{\px \t{E}_\t{total}}{\px{\t{wi}}}$

In output layer:
$$
\frac{\px \t{E}_\t{total}}{\px{\t{wi}}} = \frac{\px \t{E}_\t{total}}{\px{\t{o}_\t{out}}}.\frac{\px \t{o}_\t{out}}{\px \t{o}_\t{in}}.\frac{\px \t{o}_\t{in}}{\px \t{wi}} = -(\t{target}_\t{o} - \t{out}_\t{o}).\t{o}_\t{out}(1-\t{o}_\t{out}).\t{h}_\t{out}
$$




| Variable                                  | Value       |
| ----------------------------------------- | ----------- |
| $\frac{\px \t{E}_\t{total}}{\px{\t{w5}}}$ | $0.072157$  |
| $\frac{\px \t{E}_\t{total}}{\px{\t{w6}}}$ | $0.072691$  |
| $\frac{\px \t{E}_\t{total}}{\px{\t{w7}}}$ | $-0.042455$ |
| $\frac{\px \t{E}_\t{total}}{\px{\t{w8}}}$ | $-0.042769$ |

The update process:
$$
\t{wi}_\t{new} = \t{wi} - \eta.\frac{\px \t{E}_\t{total}}{\px{\t{wi}}} = \t{wi} - 0.5.\frac{\px \t{E}_\t{total}}{\px{\t{wi}}}
$$




| Variable | Value |
| -------- | ----- |
| $\t{w5}_\t{new}$ | $0.363922$ |
| $\t{w6}_\t{new}$          | $0.413655$ |
| $\t{w7}_\t{new}$          | $0.521228$ |
| $\t{w8}_\t{new}$          | $0.528616$ |




- **Hiden layer:**

$$
\frac{\px \t{E}_\t{total}}{\px{\t{wi}}} = \big(\Sigma_{\t{o}} \frac{\px \t{E}_\t{total}}{\px{\t{o}_\t{out}}}.\frac{\px \t{o}_\t{out}}{\px \t{o}_\t{in}}.\frac{\px \t{o}_\t{in}}{\px \t{wi}}\big). \frac{\px \t{h}_\t{out}}{\px \t{h}_\t{in}}.\frac{\px \t{h}_\t{in}}{\px \t{wi}} \\ 
\t{With } \delta_\t{o} \t{ as } [-(\t{target}_\t{o} - \t{out}_\t{o}).\t{o}_\t{out}(1-\t{o}_\t{out}).\t{h}_\t{out}]
\\
\frac{\px \t{E}_\t{total}}{\px{\t{wi}}} = \big(\Sigma_\t{o} \delta_\t{o}.\t{w}_\t{ho}).\t{h}_\t{out}.(1-\t{h}_\t{out}).\t{inp}
$$

So:

| Variable | Value |
| -------- | ----- |
| $\t{w1}_\t{new} = \t{w1} - 0,5.0,010024$ | $0.144988$ |
| $\t{w2}_\t{new} = w2 - 0,5.0,020048$ | $0.189976$ |
| $\t{w3}_\t{new} = \t{w3} - 0,5.(-0,001065)$ | $0.250532$ |
| $\t{w4}_\t{new} = \t{w4} - 0,5.(0.002130)$ | $0.301065 $ |

Done :>.

#### b.

Using the same formula in a, but with the bias:

| ![image-20200911185913892](/home/t3bol90/.config/Typora/typora-user-images/image-20200911185913892.png) |
| :----------------------------------------------------------: |
|                  **Neuron net: with bias**                   |

**The forward pass:**

| Variable                                                     | Value          |
| ------------------------------------------------------------ | -------------- |
| $\t{h1}_\t{in} = \t{w1}.\t{i1} + \t{w2}.\t{i2} + \t{b1}.1$   | $=$ $0.375500$ |
| $\t{h1}_\t{out} = \frac{1}{1+e^{-\t{h1}_\t{in}}} = \frac{1}{1+e^{-0.3755}}$ | $= 0.593270$   |
| $\t{h2}_\t{in} = \t{w3.i1 + w4.i2} +\t{b1}.1$                | $=0.392500$    |
| $\t{h2}_\t{out}$                                             | $= 0.596884$   |
| $\t{o1}_\t{in} = \t{h1.w5 + h2.w6} + \t{b2}.1$               | $= 1.105906$   |
| $\t{o1}_\t{out}$                                             | $= 0.751365$   |
| $\t{o2}_\t{in} = \t{h1.w7 + h2.w8} + \t{b2}.1$               | $= 1.224921$   |
| $\t{o2}_\t{out}$                                             | $= 0.772928$   |

**Calculate total error:**

Use same formula with a.

| Variable          | Value        |
| ----------------- | ------------ |
| $\t{E}_\t{o1}$    | $= 0.274811$ |
| $\t{E}_\t{o2}$    | $= 0.023560$ |
| $\t{E}_\t{total}$ | $= 0.298371$ |

**The backward pass:**

- **Output layer:** $\newcommand{\px}{\partial}$

Use same formula with a.

| Variable                                  | Value       |
| ----------------------------------------- | ----------- |
| $\frac{\px \t{E}_\t{total}}{\px{\t{w5}}}$ | $0.082167$  |
| $\frac{\px \t{E}_\t{total}}{\px{\t{w6}}}$ | $0.082668$  |
| $\frac{\px \t{E}_\t{total}}{\px{\t{w7}}}$ | $-0.022603$ |
| $\frac{\px \t{E}_\t{total}}{\px{\t{w8}}}$ | $-0.022740$ |

| Variable         | Value      |
| ---------------- | ---------- |
| $\t{w5}_\t{new}$ | $0.358916$ |
| $\t{w6}_\t{new}$ | $0.408666$ |
| $\t{w7}_\t{new}$ | $0.511301$ |
| $\t{w8}_\t{new}$ | $0.561370$ |

- **Hiden layer:**

Use same formula with a.

| Variable                                   | Value      |
| ------------------------------------------ | ---------- |
| $\t{w1}_\t{new} = \t{w1} - 0,5.0,0004857$  | $0.149780$ |
| $\t{w2}_\t{new} = w2 - 0,5.0,000877$       | $0.189976$ |
| $\t{w3}_\t{new} = \t{w3} - 0,5.(0.000498)$ | $0.249751$ |
| $\t{w4}_\t{new} = \t{w4} - 0,5.(0,000994)$ | $0.299502$ |

Done :>

<center><b> Have a Great Day </b></center>