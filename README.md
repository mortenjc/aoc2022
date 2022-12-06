# Advent of Code 2022
Some solutions to the Advent of Code challenge (https://adventofcode.com/)


## YouTube videos of selected solutions

### day 5
https://www.youtube.com/watch?v=Fg7wLU5xhQo

Interesting to see that he is super fast in solving the problem
because he skips parsing the graph and just manually copies it into a
relevant structure. Then struggles a bit to do the parsing.

https://www.youtube.com/watch?v=jMwr1Uc4g-o

Here I learned the trick to split data in two parts based on
a blank line (actually to consequetive newlines)

    .split('\n\n')

also learned about the pprint package and that I should definitely
look into string and list indexing

    [-1:] last entry
    [-n:] last n entries
    .extend()

### day 6
https://www.youtube.com/watch?v=LvwsB-JpJmQ

Very fast and solved this with a 3-liner. Interesting enough he solved
the first problem in a very specific way and then had to generalise
for the second solution. Main take away points

    create the set and then check it has length n
    create sets backwards to simplify range checking

    if (len >= 3) and len(set(...)) == 4
