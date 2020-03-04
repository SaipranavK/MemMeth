import sys
from MgmntMeth.initialPush import triggerPush
import globals

sys.setrecursionlimit(1500)

for block in globals.loadMemory:
    block['status']='free'
    
print(len(globals.processBlock))
total=0
for block in globals.memoryBlock:
    total+=block['size']
    
print(total)
print(len(globals.memoryBlock))

for process in globals.loadProcess:
    triggerPush(process,globals.loadMemory)

for block in globals.loadMemory:
    print("--------------------------------------------")
    print(block)

total=0
for block in globals.loadMemory:
    if block['status']=='engaged':
        total+=1
        print(block)
        
print(total)

