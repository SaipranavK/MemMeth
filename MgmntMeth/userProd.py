from MgmntMeth.NearFact import findNearestFact
import globals

# User productivity focused memory occupancy
def prodFirstPlugin(process):
    ChoiceList=[]
    for block in globals.loadMemory:
        if(block['size']>=process['size'] and block['status']=='engaged'):
            if(block['process']['relIndex']<=process['relIndex']):
                ChoiceList.append(block['process'])
            else:
                pass
    
    if(len(ChoiceList)>0):        
        print("---------------------------------------------")
        print("Clear memory to allocate ",process['name'])
        print("---------------------------------------------")
        for block in ChoiceList:
            print(block['name'])
        killProcess=input('Enter Process to be killed, None to abort load ')
    
        if(killProcess=='None'):
            print("Load aborted")
            return
        else:
            for block in ChoiceList:
                if(block['name']==killProcess):
                    print("\nKilling ",block['name'])
                    print("-------------------------------------")
                    for partition in globals.loadMemory:
                        if(partition['status']=='engaged'):
                            if(partition['process']['name']==killProcess):
                                partition['process']=process
                                print(process['name'],"Loaded into memory\n")
                                
                                remaining=partition['size']-process['size']
                                if remaining>0:
                                    size=partition['size']-remaining
                                    i=findNearestFact(size)
                                    newBlockSize=partition['size']-i
                                    if(newBlockSize>2):
                                        partition['size']=i 
                                        newBlock={'partition':str(partition['partition'])+str((len(globals.memoryBlock))),'size':newBlockSize,'status':'free'}    

                                        globals.loadMemory.append(newBlock)
                                    else:
                                        pass
                                    
                                return
    else:
        print("Cannot load Memory full")