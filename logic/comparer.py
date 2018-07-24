
import math

def get_errors_number(numberA, numberB):
    return math.pow(float(numberA) - float(numberB), 2)


def get_errors_distribution(distrA, distrB):
    errors = []
    for i in range(0, len(distrA.value.array)):
        error = math.pow(float(distrA.value.array[i].value) - float(distrB.value.array[i].value), 2)
        errors.append(error)
    return max(errors)