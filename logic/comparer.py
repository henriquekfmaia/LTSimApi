
import math

def get_errors_number(numberA, numberB):
    if numberA == numberB:
        return 0
    elif(float(numberA) != 0):
        square_difference = math.pow(float(numberA) - float(numberB), 2)
        error_relative = square_difference/math.pow(float(numberA), 2)
        return error_relative
    else:
        square_difference = math.pow(float(numberA) - float(numberB), 2)
        error_relative = square_difference/math.pow(float(numberB), 2)
        return error_relative

def get_errors_distribution(distrA, distrB):
    errors = []
    for i in range(0, len(distrA.value.array)):
        error_relative = get_errors_number(float(distrA.value.array[i].value), float(distrB.value.array[i].value))
        errors.append(error_relative)
    return max(errors)