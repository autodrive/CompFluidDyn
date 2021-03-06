import numpy as np
import pylab as py


def main():
    max_iteration = 100000
    epsilon = 1e-3

    n_width = 64
    n_height = n_width
    n_left_height = n_width / 2
    n_right_height = n_height - 1

    step_location = n_width / 2
    max_value = n_width * 1.0

    pipe = init_step_pipe(n_width, n_height, max_value, step_location, n_left_height, n_right_height)

    save_figure(pipe, 'initial.png')

    counter, max_difference = iterate(pipe, n_width, n_left_height, n_right_height, step_location, max_iteration,
                                      epsilon)
    save_figure(pipe, 'final.png')

    print("counter = %d, max_difference = %g" % (counter, max_difference))


def save_figure(pipe, filename, dpi=300):
    py.pcolor(pipe)
    py.savefig(filename, dpi=dpi)


def iterate(pipe, n_width, n_left_height, n_right_height, step_location, max_iteration, epsilon):
    for counter in range(max_iteration):
        max_difference = one_step(pipe, n_width, n_left_height, n_right_height, step_location)
        if max_difference < epsilon:
            break
    return counter, max_difference


def one_step(pipe, n_width, n_left_height, n_right_height, step_location):
    max_difference = 0

    # left side
    for j in range(1, step_location):
        for i in range(1, n_left_height):
            new_value = (pipe[i - 1, j] + pipe[i + 1, j] + pipe[i, j - 1] + pipe[i, j + 1]) * 0.25
            max_difference = max((abs(new_value - pipe[i, j]), max_difference))
            pipe[i, j] = new_value

    # right side
    for j in range(step_location, n_width - 1):
        for i in range(1, n_right_height):
            new_value = (pipe[i - 1, j] + pipe[i + 1, j] + pipe[i, j - 1] + pipe[i, j + 1]) * 0.25
            max_difference = max((abs(new_value - pipe[i, j]), max_difference))
            pipe[i, j] = new_value

    return max_difference


def init_step_pipe(n_width, n_height, max_value, step_location, n_left_height, n_right_height):
    pipe = np.zeros((n_height, n_width))
    # initialize left part
    for j in range(0, step_location):
        for i in range(n_left_height, n_height):
            pipe[i, j] = max_value

    # initializing left end
    factor = max_value * 1.0 / n_left_height
    for i in range(0, n_left_height):
        pipe[i, 0] = i * factor

    # initialize right part
    for j in range(step_location, n_width):
        for i in range(n_right_height, n_height):
            pipe[i, j] = max_value

    # initializing right end
    factor = max_value * 1.0 / n_right_height
    for i in range(0, n_right_height):
        pipe[i, -1] = i * factor

    # initialize step vertical part
    for i in range(n_left_height, n_right_height):
        pipe[i, step_location] = max_value
    return pipe


if __name__ == '__main__':
    main()
