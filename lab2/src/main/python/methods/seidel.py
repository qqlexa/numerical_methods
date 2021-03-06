# Seidel method
try:
    import util
    import matrix
except:
    try:
        from . import util
        from . import matrix
    except:
        pass


def solve(functions, eps=0.01, begin_positions=()):
    if len(begin_positions) == 0:
        begin_positions = [0 for i in range(len(functions))]

    prev_solutions = [i for i in begin_positions]
    solutions = [i for i in prev_solutions]

    is_found = False
    iterations = 0
    while not is_found:
        is_found = True
        for f in range(len(functions)):
            args = [prev_solutions[i] for i in range(f)]
            for i in range(f, len(functions)):
                args.append(solutions[i])
            solutions[f] = functions[f](args)

        for prev_solution, solution in zip(prev_solutions, solutions):
            if prev_solution - solution > eps:
                is_found = False
                break

        iterations += 1
    return solutions, iterations
