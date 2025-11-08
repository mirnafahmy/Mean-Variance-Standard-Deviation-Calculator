import numpy as np

def calculate(list):
    if len(lists) != 9:
        print('List must contain nine numbers.')

    arr = np.array(lists).reshape(3,3)
    
    mean = [list(np.mean(arr, axis=0)), 
            list(np.mean(arr, axis=1)), np.mean(arr)]
    
    vari = [list(np.var(arr, axis=0)), 
                list(np.var(arr, axis=1)), np.var(arr)]
    
    std_dev = [list(np.std(arr, axis=0)), 
               list(np.std(arr, axis=1)), np.std(arr)]
    
    max_v = [list(np.max(arr, axis=0)), 
               list(np.max(arr, axis=1)), np.max(arr)]
    
    min_v = [list(np.min(arr, axis=0)), 
               list(np.min(arr, axis=1)), np.min(arr)]
    
    sum_v = [list(np.sum(arr, axis=0)), 
               list(np.sum(arr, axis=1)), np.sum(arr)]

    calculations = {
        'mean': mean,
        'variance': vari,
        'standard deviation': std_dev,
        'max': max_v,
        'min': min_v,
        'sum': sum_v
    }

    return calculations
