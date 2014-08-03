# About recursion-trees

There are some "rules of thumb" to follow when solving recursions.

## 1) Find the height of the tree and the cost of the leaves

This one is easy. We just have to figure out what happens at the lowest level (where the leaves are) when the size of each node's input is the least (i.e. 1, most of the times). In other words, for example, if the size of input of each node at level i is (n/k)^i we need to solve the equation (n/k)^i = 1.

Remember that if the tree has height X it means the number of levels is X + 1 (0..X).

To find the cost of the leaves just find the total number of leaves and multiply by the constant cost. Remember to select a bound and add it to the final recurrence.

## 2) Compute the total cost at each level

At level i the total cost is equal to N * CN where N is the number of nodes and CN is the cost per node.

## 3) Guess a complexity for the lowest level

This step is also quite easy since we just have to multiply the number of leaves by the cost of each node which, at the lowest level, is constant. Let's suppose that at each level we have 3 children for each node from the previous call and that the total height of the tree is log4(n). The total number of nodes at the lowest level is 3^log4(n). We can use a logarithms' property that states:

C^logB(A) = A^logB(C)

So we have something like n^log4(3) and we can easily see that the complexity is O(n^log4(3)). This will be added as a tail to our final recurrence.

## 4) Express the total cost as a summation

We compute the total cost for the first N-1 levels (excluding the leaves) and we add it to the complexity figured out before.

The trick is to express the summation as a geometric progression so we can use predefined formulas to turn it into a less complex form.

## 5) Figure out if the bound we found is a tight one

This is kind of easily verifiable by looking at the contribution of the root's cost. For example if we guessed O(n^2) and the root has a cost of cn^2 it's easy to see that even in the best case, with only one call and a size of input greater than the base value, we have a contribution in the same order of growth of O(n^2). Which means it is also Om(n^2) and so Th(n^2).
