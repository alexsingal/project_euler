#sum of squares formula: n(n+1)(2n+1)/6
#square of sums formula: n(n+1)/2

sum_of_squares = 100*101*201/6
square_of_sums = (100*101/2)**2

print abs(sum_of_squares - square_of_sums)