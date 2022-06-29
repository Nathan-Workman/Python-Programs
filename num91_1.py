import math

##p_0 = float(input("Enter p_0:  "))
numbers = [2.0, 1.666666666666667, 1.727272727272727, 1.732142857142857,1.732050680431722, 1.732050807565499]

for n in range(5):
    
##    p_1 = float(input("Enter p_1:  "))
    
    currentEps = abs(numbers[n+1] - math.sqrt(3))
    lastEps = math.pow(abs(numbers[n] - math.sqrt(3)), 1.618)
    
    currentRatio = currentEps/lastEps
    
##    p_0 = p_1
    
    print(f'{currentEps:.15f}     {lastEps:.15f}    {currentRatio:.15f}')
    