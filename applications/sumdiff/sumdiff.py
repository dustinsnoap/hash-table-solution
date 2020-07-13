"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# $%$Start
sums = {}
diffs = {}

# Loop through every 2-combination of elements in `q`, storing all the
# pairs that form a certain sum, and all the pairs that form a certain
# difference.
for i in q:
    for j in q:

        # Sums
        s = f(i) + f(j)

        # Store the pair that makes this sum
        if s in sums:
            sums[s].append((i, j))
        else:
            sums[s] = [(i, j)]

        # Differences
        d = f(i) - f(j)

        # Store the pair that makes this difference
        if d in diffs:
            diffs[d].append((i, j))
        else:
            diffs[d] = [(i, j)]

# If a key (representing the sum or difference) appears in `sums` AND in
# `diffs`, all those sums must equal all those diffs.
for skey in sums:
    if skey in diffs:

        # And if they do, print out all combinations of sums and
        # differences that compute equally.
        for s in sums[skey]:
            for d in diffs[skey]:
                a, b, c, d = s[0], s[1], d[0], d[1]

                # Make sure it's right
                assert(f(a) + f(b) == f(c) - f(d))

                print(f'f({a}) + f({b}) = f({c}) - f({d})'
                      f'    {f(a)} + {f(b)} = {f(c)} - {f(d)}')
# $%$End
