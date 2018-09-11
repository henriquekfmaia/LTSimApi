import math
import logic.comparer as co

def add_flows(flowA, flowB):
    flowA.waterFlow.value = float(flowA.waterFlow.value) + float(flowB.waterFlow.value)
    totalMass = float(flowA.massFlow.value) + float(flowB.massFlow.value)
    if totalMass == 0:
        totalMass = 1
    wA = float(flowA.massFlow.value)/totalMass
    wB = float(flowB.massFlow.value)/totalMass
    flowA.massFlow.value = totalMass
    arraySum = 0
    for i in range(1, len(flowA.sizeDistribution.value.array)):
        flowA.sizeDistribution.value.array[i].value = wA*float(flowA.sizeDistribution.value.array[i].value) + wB*float(flowB.sizeDistribution.value.array[i].value)
        arraySum += flowA.sizeDistribution.value.array[i].value
    flowA.sizeDistribution.value.array[0].value = 100 - arraySum
    return flowA

def restart_flow(flow):
    flow.waterFlow.value = 0
    flow.massFlow.value = 0
    for i in flow.sizeDistribution.value.array:
        i.value = 0
    flow.sizeDistribution.value.array[0].value = 100
    return flow

def is_flow_known(flow):
    return(hasattr(flow.waterFlow, 'value') and hasattr(flow.massFlow, 'value') and hasattr(flow.sizeDistribution, 'value'))
    #return (flow.waterFlow.value == None or flow.massFlow.value == None or flow.sizeDistribution.value == None)

def get_flow_errors(flowA, flowB):
    errors = []
    errors.append(co.get_errors_number(flowA.waterFlow.value, flowB.waterFlow.value))
    errors.append(co.get_errors_number(flowA.massFlow.value, flowB.massFlow.value))
    errors.append(co.get_errors_distribution(flowA.sizeDistribution, flowB.sizeDistribution))
    return max(errors)


        
