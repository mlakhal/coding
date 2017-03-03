"""Random walk problem.
Starting from the origin, you can either move forward (+1),
or backward (-1) at each step.
Determine the probability of going back to the origin, after "n" moves.

Author: Mohamed Lakhal

"""

import argparse

def generate_paths(n):
    """Generate all the possible path.

    Args:
        n (int): number of moves

    Returns:
        list[list]: all possible moves

    """
    tmp, idx = n, 0
    paths = [[0] for _ in xrange(2 ** n)]
    while tmp > 0:
        for i in xrange(2 ** n):
            if idx % 2 == 0:
                paths[i].append(paths[i][-1] + 1)
            else:
                paths[i].append(paths[i][-1] - 1)

            idx += 1

        paths.sort()
        tmp -= 1

    return paths

def main(n):
    paths = generate_paths(n)
    back_to_origin = sum([1 for v in paths if v[-1] == 0])
    prob = back_to_origin / float(len(paths))

    print("-==-" * 10)
    print("Number of solution that goes back to the origin:{}".format(\
                    back_to_origin))
    print("-==-" * 10)
    print("Probability: {}".format(prob))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--moves",
                        type=int, default=4,
                        help="Number of moves")
    args = parser.parse_args()
    main(args.moves)
