import numpy as np
import time
import matplotlib.pylab as plt

def rook(n, num_iter):
    start = time.time()
    ## Set up board and attacked counter
    board = range(n**2)
    attacked = 0
    safe = []
    for i in range(num_iter):
        ## Randomly assign rooks 
        rooks = np.random.choice(board, n, replace=False)
        rows = set([rook / n for rook in rooks])
        cols = set([rook % n for rook in rooks])
        ## If rooks cover all cols or all rows, there's no place where a king can't be attacked
        safe_rows = n - len(rows)
        safe_cols = n - len(cols)
        num_safe = safe_rows * safe_cols
        safe.append(num_safe)
        if num_safe == 0: 
            attacked += 1
    end = time.time()
    print("Time Elapsed: %.4f" %(end-start))
    print("After %d iterations with %d rooks, the probability of at least one king being safe is  %.4f" %(num_iter, n, float(num_iter - attacked) / num_iter))
    return safe

def summary(arr):
    mean, st_dev = np.mean(arr), np.std(arr)
    plt.hist(x=arr, bins='auto')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Safe Grid Distribution')
    plt.show()
    print("Mean is %.4f and Standard Deviation is %.4f" %(np.mean(arr), np.std(arr)))
    
summary(rook(5, 100000))

#summary(rook(15, 100000))



