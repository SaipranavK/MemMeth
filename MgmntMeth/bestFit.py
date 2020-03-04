from MgmntMeth.userProd import prodFirstPlugin
# Find the bestfit partition for process
def bestFit(process,memoryBlock):
    flag=0
    partition=None
    for i in range(0,len(memoryBlock)):
        if(process['size']<=memoryBlock[i]['size']):
            currentSize=memoryBlock[i]['size']
            if(flag!=1):
                assignedSize=currentSize
                partition=memoryBlock[i]['partition']
                flag=1
                
            if(currentSize<assignedSize):
                assignedSize=currentSize
                partition=memoryBlock[i]['partition']
                
    if(partition==None):
        print("No Space Available to Allocate for:",process,"\n") 
        prodFirstPlugin(process) #Comment to evaluate BestFit only
        return -1
    else:    
        print("partition for:",process,"-",partition)
        return partition