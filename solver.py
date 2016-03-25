import empirical

class Solver(object):
  def solve(self, x, y):
    solution = x + y
    return solution

empirical.run(Solver())
