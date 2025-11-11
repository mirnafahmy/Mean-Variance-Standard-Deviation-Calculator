import numpy as np

def calculate(list):
    if len(list) != 9:
        print('List must contain nine numbers.')

    arr = np.array(list).reshape(3,3)
    print(arr)

    mean = [np.mean(arr,axis=0).tolist(),
            np.mean(arr,axis=1).tolist(),
            np.mean(arr)]
    
    vari = [np.var(arr, axis=0).tolist(), 
            np.var(arr, axis=1).tolist(), 
            np.var(arr)]
    
    std_dev = [np.std(arr, axis=0).tolist(), 
               np.std(arr, axis=1).tolist(), 
               np.std(arr)]
    
    max_v = [np.max(arr, axis=0).tolist(), 
            np.max(arr, axis=1).tolist(), 
            np.max(arr)]
    
    min_v = [np.min(arr, axis=0).tolist(), 
            np.min(arr, axis=1).tolist(), 
            np.min(arr)]
    
    sum_v = [np.sum(arr, axis=0).tolist(), 
            np.sum(arr, axis=1).tolist(), 
            np.sum(arr)]

    calculations = {
        'mean': mean,
        'variance': vari,
        'standard deviation': std_dev,
        'max': max_v,
        'min': min_v,
        'sum': sum_v
    }

    return calculations
