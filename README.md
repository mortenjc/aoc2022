# Advent of Code 2022
Some solutions to the Advent of Code challenge (https://adventofcode.com/)

## YouTube videos of selected solutions
After solving the puzzles I go and check videos of some
of the leaderboard contributers (often just picking the
first that comes up from the search). I do this to try to
learn about different approaches to attacking the problem,
language features I don't know and the use of additional
packages.

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

### day 7
https://www.youtube.com/watch?v=ZPM5xclRInk

My approach was the same, just took me a lot longer, but
I wasted time on a too complicated parser and also working
around =+ operations on non-existing keys. I also used a weird
logic to calculate dir names and removing the double '/' which
he just ignored. Main learnings:

    use defaultdict (from collections import defaultdict)
    sizes = defaultdict(int)

    sometimes list comprehension is not necessary
