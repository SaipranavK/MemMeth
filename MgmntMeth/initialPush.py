from MgmntMeth.bestFit import bestFit
from MgmntMeth.NearFact import findNearestFact
from datetime import datetime
import globals

def triggerPush(process,memoryBlock):
    # Initial memory commit 
    def firstPush(process,memoryBlock,partition,tempMem):
        if(partition==-1):
            return
        
        index=-1
        for i in range(0,len(memoryBlock)):
            if(partition==memoryBlock[i]['partition']):
                index=i
                break

        if(memoryBlock[index]['status']=='free'):
            memoryBlock[index]['process']=process
            memoryBlock[index]['startTime']=datetime.now().time()
            memoryBlock[index]['status']='engaged'
            
            remaining=memoryBlock[index]['size']-process['size']
            
            if(remaining>0):
                size=memoryBlock[index]['size']-remaining
                i=findNearestFact(size)
                newPartSize=memoryBlock[index]['size']-i
                print(newPartSize)
                if(newPartSize>2):
                    memoryBlock[index]['size']=i
                    newBlock={'partition':str(memoryBlock[index]['partition'][0])+str((len(memoryBlock))),'size':newPartSize,'status':'free'}    

                    globals.loadMemory.append(newBlock)
                else:
                    pass

        else:
            for block in tempMem:
                if(block['partition']==partition):
                    tempMem.remove(block)
            if(len(tempMem)>0):
                partition=bestFit(process,tempMem)
                firstPush(process,memoryBlock,partition,tempMem)

            else:
                print("MemoryFull")
                exit(1)
                
    partition=bestFit(process,memoryBlock)
    tempMem=[]
    for blocks in memoryBlock:
        tempMem.append(blocks)
    
    firstPush(process,memoryBlock,partition,tempMem)