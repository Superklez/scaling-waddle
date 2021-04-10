import numpy as np
import matplotlib.pyplot as plt

def discreteKronecker(arr, m=0):
    crr = np.zeros(arr.shape)
    crr[arr == m] = 1
    return crr

def discreteHeaviside(arr, m=0):
    crr = np.zeros(arr.shape)
    crr[arr >= m] = 1
    return crr

def num1(letter:str='a'):
    if letter == 'a':
        x = np.arange(0, 11)
        y = discreteKronecker(x, 5)

        fig, ax = plt.subplots(1, 1, figsize=(7, 5))
        ax.scatter(x, y, zorder=4)
        for pt in zip(x, y):
            ax.plot([pt[0],pt[0]], [0,pt[1]], c='C0', zorder=3)

        ax.set_xlabel('$n$')
        ax.set_ylabel('$y[n]$')
        ax.set_xticks(x)

        ax.axhline(y=0, color='k', zorder=2)
        ax.axvline(x=0, color='k', zorder=2)
        ax.grid(zorder=1)

        plt.tight_layout()
        plt.show()

    elif letter == 'b':
        x = np.arange(-1, 16)
        y = discreteHeaviside(x, 7)

        fig, ax = plt.subplots(1, 1, figsize=(7, 5))
        ax.scatter(x, y, zorder=4)
        for pt in zip(x, y):
            ax.plot([pt[0],pt[0]], [0,pt[1]], c='C0', zorder=3)

        ax.set_xlabel('$n$')
        ax.set_ylabel('$y[n]$')
        ax.set_xticks(x)

        ax.axhline(y=0, color='k', zorder=2)
        ax.axvline(x=0, color='k', zorder=2)
        ax.grid(zorder=1)

        plt.tight_layout()
        plt.show()

def num2(letter:str='a'):
    if letter == 'a':
        x = np.arange(-5, 6)
        y = discreteHeaviside(x)

        fig, ax = plt.subplots(1, 1, figsize=(7, 5))
        ax.scatter(x, y, zorder=4)
        for pt in zip(x, y):
            ax.plot([pt[0],pt[0]], [0,pt[1]], c='C0', zorder=3)

        ax.set_xlabel('$n$')
        ax.set_ylabel('$x[n]$')
        ax.set_xticks(x)

        ax.axhline(y=0, color='k', zorder=2)
        ax.axvline(x=0, color='k', zorder=2)
        ax.grid(zorder=1)
        plt.tight_layout()
        plt.show()

    elif letter == 'b':
        x = np.arange(-6, 11)
        y = 0.5**x * discreteHeaviside(x)

        fig, ax = plt.subplots(1, 1, figsize=(7, 5))
        ax.scatter(x, y, zorder=4)
        for pt in zip(x, y):
            ax.plot([pt[0],pt[0]], [0,pt[1]], c='C0', zorder=3)

        ax.set_xlabel('$n$')
        ax.set_ylabel('$I[n]$')
        ax.set_xticks(x)

        ax.axhline(y=0, color='k', zorder=2)
        ax.axvline(x=0, color='k', zorder=2)
        ax.grid(zorder=1)

        plt.tight_layout()
        plt.show()

    elif letter == 'c':
        x = np.arange(-3, 8)
        y = []

        for n in x:
            res = []
            for k in range(x[0]-10, x[-1]+10):
                if k>=0 and n-k>=0:
                    res.append(0.5**(n-k))
            y.append(sum(res))

        fig, ax = plt.subplots(1, 1, figsize=(7, 5))
        ax.scatter(x, y, zorder=4)
        for pt in zip(x, y):
            ax.plot([pt[0],pt[0]], [0,pt[1]], c='C0', zorder=3)

        ax.set_xlabel('$n$')
        ax.set_ylabel(r'$x[k] \ast I[n-k]$')
        ax.set_xticks(x)

        ax.axhline(y=0, color='k', zorder=2)
        ax.axvline(x=0, color='k', zorder=2)
        ax.grid(zorder=1)

        plt.tight_layout()
        plt.show()

    elif letter == 'd':
        n = 4
        x = np.arange(-4, 8)
        y = 2*discreteHeaviside(x) * (1 - 0.5**(x+1))

        fig, ax = plt.subplots(1, 1, figsize=(7, 5))
        ax.scatter(x, y, zorder=4)
        for pt in zip(x, y):
            ax.plot([pt[0],pt[0]], [0,pt[1]], c='C0', zorder=3)

        ax.set_xlabel('$n$')
        ax.set_ylabel('$y[n]$')
        ax.set_xticks(x)

        ax.axhline(y=0, color='k', zorder=2)
        ax.axvline(x=0, color='k', zorder=2)
        ax.grid(zorder=1)

        plt.tight_layout()
        plt.show()

def num3(letter:str='b'):
    x = np.arange(-5, 13)
    y = discreteKronecker(x, 1) + 2*discreteKronecker(x, 2) + \
        3*discreteKronecker(x, 3) + 3*discreteKronecker(x, 4) + \
        2*discreteKronecker(x, 5) + discreteKronecker(x, 6)

    fig, ax = plt.subplots(1, 1, figsize=(7, 5))
    ax.scatter(x, y, zorder=4)
    for pt in zip(x, y):
        ax.plot([pt[0],pt[0]], [0,pt[1]], c='C0', zorder=3)

    ax.set_xlabel('$n$')
    ax.set_ylabel('$y[n]$')
    ax.set_xticks(x)

    ax.axhline(y=0, color='k', zorder=2)
    ax.axvline(x=0, color='k', zorder=2)
    ax.grid(zorder=1)

    plt.tight_layout()
    plt.show()

def num4(letter:str='b'):
    x = np.arange(-3, 11)
    y = -discreteKronecker(x, 1) + 2*discreteKronecker(x, 2) - \
        discreteKronecker(x, 3) - 2*discreteKronecker(x, 4) + \
        3*discreteKronecker(x, 5) - 2*discreteKronecker(x, 6)

    fig, ax = plt.subplots(1, 1, figsize=(7, 5))
    ax.scatter(x, y, zorder=4)
    for pt in zip(x, y):
        ax.plot([pt[0],pt[0]], [0,pt[1]], c='C0', zorder=3)

    ax.set_xlabel('$n$')
    ax.set_ylabel('$y[n]$')
    ax.set_xticks(x)

    ax.axhline(y=0, color='k', zorder=2)
    ax.axvline(x=0, color='k', zorder=2)
    ax.grid(zorder=1)

    plt.tight_layout()
    plt.show()

def num5(letter:str='a'):
    x = np.arange(-10, 11)
    y = []

    for n in x:
        res = []
        for k in range(x[0]-10, x[-1]+10):
            if n-k>=0:
                res.append(0.5**(n-k) * np.sin(n*np.pi/6))
        y.append(sum(res))

    fig, ax = plt.subplots(1, 1, figsize=(7, 5))
    ax.scatter(x, y, zorder=4)
    for pt in zip(x, y):
        ax.plot([pt[0],pt[0]], [0,pt[1]], c='C0', zorder=3)

    ax.set_xlabel('$n$')
    ax.set_ylabel(r'$y[n]$')
    ax.set_xticks(x)

    ax.axhline(y=0, color='k', zorder=2)
    ax.axvline(x=0, color='k', zorder=2)
    ax.grid(zorder=1)

    plt.tight_layout()
    plt.show()

letters_cache = {
    '1':['a', 'b'],
    '2':['a', 'b', 'c', 'd'],
    '3':['b'],
    '4':['b'],
    '5':['a']
}

functions_cache = {
    '1':num1,
    '2':num2,
    '3':num3,
    '4':num4,
    '5':num5
}

if __name__ == '__main__':
    print(f'Choose a number in: {list(range(1, 6))}')
    number = int(input('Number: ').strip())

    while number not in range(1, 6):
        print('-'*30)
        print(f'ERROR: Number provided not in {list(range(1, 6))}')
        number = int(input('Number: ').strip())

    print('-'*30)
    letters = letters_cache[str(number)]
    print(f'Choose a letter in: {letters}')
    letter = input('Letter: ').strip()
    while letter not in letters:
        print('-'*30)
        print(f'ERROR: Letter provided not in {letters}')
        letter = input('Letter: ').strip()

    print('-'*30)
    print(f'Selected number: {number}')
    print(f'Selected letter: {letter}')

    functions_cache[str(number)](letter)
