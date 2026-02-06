#Mean-Variance-Standard Deviation Calculator
#Create a function named calculate() that uses NumPy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3x3 matrix.

#The input of the function should be a list containing 9 digits. The function should convert the list into a 3x3 Numpy array, and then return a dictionary 
#containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

#The returned dictionary should follow this format:
{
  'mean': ['axis1', 'axis2', 'flattened'], #axis1=columns axis2=rows
  'variance': ['axis1', 'axis2', 'flattened'],
  'standard deviation': ['axis1', 'axis2', 'flattened'],
  'max': ['axis1', 'axis2', 'flattened'],
  'min': ['axis1', 'axis2', 'flattened'],
  'sum': ['axis1', 'axis2', 'flattened']
}

#If a list containing less than 9 elements is passed into the function, it should raise a ValueError exception with the message: "List must contain nine 
#numbers." The values in the returned dictionary should be lists and not Numpy arrays.

#For example, calculate([0,1,2,3,4,5,6,7,8]) should return:
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}

import numpy as np
def mean(after): #This function obtain the mean value of the columns, rows and flattened items from the array
    meanValues = [
        [round(float(after[:,0].mean()),2), round(float(after[:,1].mean()),2), round(float(after[:,2].mean()),2)],
        [round(float(after[0,].mean()),2), round(float(after[1,].mean()),2), round(float(after[2,].mean()),2)],
        round(float(after.mean()),2)
        ]
    return meanValues

def variance(after): #This function obtain the variance value of the columns, rows and flattened items from the array
    varianceValues = [
        [round(float(after[:, 0].var()),2), round(float(after[:, 1].var()),2), round(float(after[:, 2].var()),2)], 
        [round(float(after[0,].var()),2), round(float(after[1,].var()),2), round(float(after[2,].var()),2)], 
        round(float(after.var()),2)
        ]
    return varianceValues

def std(after): #This function obtain the std value of the columns, rows and flattened items from the array
    stdValues = [
        [round(float(after[:,0].std()),2), round(float(after[:,1].std()),2), round(float(after[:,2].std()),2)], 
        [round(float(after[0,].std()),2), round(float(after[1,].std()),2), round(float(after[2,].std()),2)], 
        round(float(after.std()))
        ]
    return stdValues

def max(after): #This function obtain the max value of the columns, rows and flattened items from the array
    maxValues = [
        [float(after[:,0].max()), float(after[:,1].max()), float(after[:,2].max())], 
        [float(after[0,].max()), float(after[1,].max()), float(after[2,].max())], 
        float(after.max())
        ]
    return maxValues

def min(after): #This function obtain the min value of the columns, rows and flattened items from the array
    minValues = [
        [float(after[:, 0].min()), float(after[:, 1].min()), float(after[:, 2].min())], 
        [float(after[0,].min()), float(after[1,].min()), float(after[2,].min())], 
        float(after.min())
        ]
    return minValues

def suma(after): #This function obtain the sum of all values of the columns, rows and flattened items from the array
    sumValues = [
        [float(after[:, 0].sum()), float(after[:, 1].sum()), float(after[:, 2].sum())], 
        [float(after[0,].sum()), float(after[1,].sum()), float(after[2,].sum())], 
        float(after.sum())
        ]
    return sumValues

numValues = [7, 3, 9, 4, 8, 2, 1, 10, 6]
def calculate(numValues):
    if len(numValues) < 9:
       raise ValueError('List must contain nine numbers')
    before = np.array(numValues)
    after = before.reshape(3, 3)
    print(after)
    output = {}
    output['mean'] = mean(after)
    output['variance'] = variance(after)
    output['std'] = std(after)
    output['max'] = max(after)
    output['min'] = min(after)
    output['sum'] = suma(after)
    return output
print(calculate(numValues))

#Iterate the dictionary and search specify elements (optional)
def obtener_valores(dict, dato):
    for k in dict:
        if k == dato:
            return dict[k][2]
    return 'dato no encontrado'
#print(obtener_valores(calculate(numValues), 'variance'))
