import numpy as np


def compute(elements):
    x = [elements[:, 0], elements[:, 1], elements[:, 2]]
    print(x)
    y = elements[0:2, 0:2]
    print(y)
    print(y.shape)
    print(sum(elements))
    print(sum(x))
    print(np.sum(x))
    print(np.sum(elements))
    print(np.min(x))
    print(np.max(x))
    print(np.mean(x))
    z = np.multiply(x, x)
    print(z)
    print(np.mean(z))
    print(np.std(z))
    x1 = np.zeros((3, 3), complex)
    print(x1)
    print(type(x1[0, 0]))
    x2 = np.ones((3, 3), float)
    print(x2)
    print(type(x2[0, 0]))
    for i in x:
        print(i)
    x_sum = 0
    for i in x:
        for j in i:
            x_sum = x_sum + j
    print(x_sum)
    x_sum2 = 0
    for i in np.nditer(x):
        x_sum2 = x_sum2 + i[0]
    print(x_sum2)


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    inputs = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    compute(inputs)
