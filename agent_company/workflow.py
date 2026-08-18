from .db import add_activity

state={
 'CEO':'READY',
 'Research':'WAITING',
 'Developer':'WAITING',
 'Marketing':'WAITING'
}

def start_workflow(goal):
    state['CEO']='WORKING'
    add_activity('老板目标：'+goal)
    add_activity('CEO 正在分析目标并制定计划')

    state['CEO']='COMPLETED'
    state['Research']='WORKING'
    add_activity('CEO 分配任务：Research 开始市场调查')

    return state
