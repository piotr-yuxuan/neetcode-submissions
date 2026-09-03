import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, *args):
        if 1 == len(args):
            radius = args[0]
            result = round(math.pi * (radius**2), 2)
        else:
            length, width = args
            result = length * width

        return result
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
