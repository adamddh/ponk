# PONK

Just a simple repository currently containing a few classes and files to implement poker logic. Made for the purposes of learning and reinforcing some skills, such as unit testing, Enums in python, and algorithmic complexity.

### To Do:

Compare two hands, determine the winner. Also, if the turn and the river are not yet visible, determine who has better odds and what thier outs are. 

### Why deal with algorithms?

2 reasons, 1 real, 1 yet undetermined.

1) __real__: All of these algorithms should be executable in $O(n)$ time, with $n$ being the amount of cards in the hand. While $2 < n < 7$, meaning this analysis of complexity is not a meaningful problem, it is good to exercise and demonstrate that these algorithms do no have to be written in computationally more complex ways. _For example_ the algorithm determining if a straight is present in a hand can easily be brute forced via a nested _for_ loop, but this can also be done more elegantly in 2 linear passes over the data (assuming a sorting algorithm is not used). 
2) __undetermined__ _for now_: In comparing two hands, I could be running through a few hundred possible scenarios, determining the winner based on yet unseen cards. In this case, I do want my algorithms to be fast. _This could mean I want to switch to a faster $O(n^2)$ algorithm if its faster than $O(n)$ for $n < 7$._ This will take some testing, but is fun to do anyway. 