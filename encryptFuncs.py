import numpy as np

def shiftRow(key):
    numMatrs = int(len(key)/16)
    work = np.array([4,4,numMatrs])
    #for i in range(numMatrs):
    workHold = np.reshape(key[0*16:(0+1)*16],[4,4])
    print(workHold)
    hold = workHold
    for it in range(len(workHold[:,0])-1):
    	
    	for it2 in range(len(workHold[0,:])-1):
    		print((it2+it) % 4)
    		
    		workHold[it,it2] = hold[it,((it2+it) % 4)]
    #work = workHold
    print(workHold)
    #work[:,:,0] = workHold
    workHold = np.reshape(workHold,16)

    print(workHold)
    return(work)

shiftRow(np.array([1,2,4,3,2,6,6,4,4,2,5,3,32,4,5,3]))

