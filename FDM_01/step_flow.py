import numpy as np
import pylab as py


def main():
    n_width = 64
    n_height = n_width
    n_left_height = n_width / 2
    n_right_height = n_height - 1

    step_location = n_width / 2
    max_value = n_width * 1.0

    pipe = init_step_pipe(n_width, n_height, max_value, step_location, n_left_height, n_right_height)

    py.pcolor(pipe)
    py.show()


def init_step_pipe(n_width, n_height, max_value, step_location, n_left_height, n_right_height):
    pipe = np.zeros((n_height, n_width))
    # initialize left part
    for j in range(0, step_location):
        pipe[n_left_height, j] = max_value

    # initialize right part
    for j in range(step_location, n_width):
        pipe[n_right_height, j] = max_value

    # initialize vertical part
    for i in range(n_left_height, n_right_height):
        pipe[i, step_location] = max_value
    return pipe


if __name__ == '__main__':
    main()
