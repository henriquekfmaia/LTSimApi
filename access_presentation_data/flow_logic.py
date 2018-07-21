def add_flows(flowA, flowB):
    flowA.waterFlow.value = float(flowA.waterFlow.value) + float(flowB.waterFlow.value)
    flowA.massFlow.value = float(flowA.massFlow.value) + float(flowB.massFlow.value)
    for i in range(0, len(flowA.sizeDistribution.value.array)):
        flowA.sizeDistribution.value.array[i].value = float(flowA.sizeDistribution.value.array[i].value) + float(flowB.sizeDistribution.value.array[i].value)
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