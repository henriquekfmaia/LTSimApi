def add_flows(flowA, flowB):
    flowA.waterFlow.value += flowB.waterFlow.value
    flowA.massFlow.value += flowB.massFlow.value
    for i in range(0, len(flowA.sizeDistribution.value.array)):
        flowA.sizeDistribution.value.array[i].value += flowB.sizeDistribution.value.array[i].value
    return flowA

def restart_flow(flow):
    flow.waterFlow.value = 0
    flow.massFlow.value = 0
    for i in flow.sizeDistribution.value.array:
        i.value = 0
    return flow

def is_flow_blank(flow):
    return (flow.waterFlow.value == None or flow.massFlow.value == None or flow.sizeDistribution.value == None)