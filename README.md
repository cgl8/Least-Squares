# Least-Squares

A fun way to add a line of best fit to a dataset using the Least-Squares method. This project is to supplement my OWN LEARNING.


## Method

The parameters of a line of best fit is calculated using the normal equations. 
Given a matrix equation $A\vec{x} = \vec{b}$, the normal equation is that which minimises the sum of the square differences:

<p align="center">
$A^TA\hat{\vec{x}} = A^T\vec{b} \;\;\;\Rightarrow \;\;\;\hat{\vec{x}} = (A^TA)^{-1}A^T\vec{b}$
</p>

This can be used with the following matrix equations of the form $A\vec{x} = \vec{b}$ to obtain the parameters to an equation that will minimise the cost.
```math
\begin{bmatrix}
1 & x_1 \\
1 & x_2 \\
1 & x_3 \\
\vdots \\
1 & x_n
\end{bmatrix} \begin{bmatrix}
c \\ m
\end{bmatrix} = \begin{bmatrix}
y_1 \\
y_2 \\
y_3 \\
\vdots \\
y_n
\end{bmatrix}
,\ \ \ \ \ \ \ 
\begin{bmatrix}
1 & ln(x_1) \\
1 & ln(x_2) \\
1 & ln(x_3) \\
\vdots \\
1 & ln(x_n)
\end{bmatrix} \begin{bmatrix}
c \\ m
\end{bmatrix} = \begin{bmatrix}
y_1 \\
y_2 \\
y_3 \\
\vdots \\
y_n
\end{bmatrix},
\ \ \ \ etc..
```
## Proof

There exists some $\hat{\vec{x}}$ s.t. $A\hat{\vec{x}}$ is the best approximation of $\vec{b}$ in the column space of the $m \times n$ matrix $A$. By the best approximation theorem, the best approximation of $\vec{b}$ in $Col(A)$ is:  

<p align="center">
$\hat{\vec{b}} = proj_{Col(A)}(\vec{b})$  
</p>

Any least squares solution must thus satisfy the equation $A\hat{\vec{x}} = proj_{Col(A)}(\vec{b})$. This equation must be consistent, since $\hat{\vec{b}}$ is an element of the column space of A.

We know that $\vec{b} - \hat{\vec{b}}$ must be orthogonal to the column space of A, hence 

```math
0\,=\;\;<\,\!a_i, \vec{b} - \hat{\vec{b}}>\;\; = \;\; <\,\!a_i, \vec{b} - A\hat{\vec{x}}>
```

where $a_i$ represents the columns of $A$ for all $i = 1,2,3,\ldots,n$. Thus:

```math
\begin{eqnarray}

a_i^T(\vec{b}-A\hat{\vec{x}}) &=& 0\\

A^T(\vec{b}-A\hat{\vec{x}}) &=& \vec{0} \ \ \ (since\ \  \vec{u}\cdot\vec{v} = \vec{u}^T\vec{v})\\ <!-- TODO: Should equal zero vector, NOT 0. -->

A^T\vec{b} - A^TA\hat{\vec{x}} &=& \vec{0}\\
\\
\\

\therefore\;\; A^TA\hat{\vec{x}} &=& A^T\vec{b} \;\;\;\; \blacksquare

\end{eqnarray}
```

