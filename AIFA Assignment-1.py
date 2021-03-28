#!/usr/bin/env python
# coding: utf-8

# In[6]:


## AIFA Assignment - 1
## Submitted by: 
##       Arnab Moitra (17MI31008)
##       Naman Agrahari (17MI33009)

def all_pairs_shortest_path (arr): ## arr -> Adjacency Matrix
    ''' Finds the Shortest path among all paris of nodes
    
        Parameters:
            arr: Adjacency Matrix having arr[i][j] = inf if i and j aren't directly connected
        
        Returns:
            A n*n matrix apst where apst[i][j] = shortest path between i and j
    '''
    
    apst = [[9999 for i in range(len(arr[0]))]for j in range(len(arr))]
    for i in ranage(len(arr)):
        for j in range(len(arr[0])):
            apst[i][j] = arr[i][j]
            if i==j:
                apst[i][j]=0
            apst[j][i] = apst[i][j]
            
    for k in range(len(arr)):
        for i in range(len(arr)):
            for j in range(len(arr)):
                apst[i][j] = min(apst[i][j],apst[i][k]+apst[k][j])
                
    return apst  ## Returns the array for all pairs shortest path

def min_time (ev, arr, dist): ##arr -> Adjacency List 
    ''' Takes an EV at a time and returns the Minimum time it takes to reach to it's destination
    
        Parameters:
            ev = Specifications of an EV
            arr = Adjacency List
            dist = The All Pairs Shortest Path matrix
            
        Returns:
            Minimum Time for that EV to reach to it's destination from the Source
            Path that is to be followed by EV
    '''
    
    ## Returns the Minimum time to reach the destination
    ## Also returns the path to be followed by the EV
    
    start=ev[0]
    end=ev[1]
    ini_charge= ev[2]
    capacity=ev[5]
    c_rate=ev[3]
    d_rate=ev[4]
    speed= ev[6]
    from collections import Counter
    visited=Counter([])
    import heapq
    q=[(0,start,ini_charge)]  
    if ini_charge!=capacity:
        q.append(((capacity-ini_charge)/c_rate,start,capacity))
    heapq.heapify(q) ## Initialize the Heap with 2 elements one with full charge and other with initial given charge 
    path=[]
    while 1:
        k=heapq.heappop(q)
        visited[k[1]]+=1  ## The city is visited
        path.append(k)  ## Append the city visited to the path
        if k[1]==end:
            break
        for item in arr[k[1]]: 
            if visited[item]==0: ## Only for un-visited cities
                c_now=(k[2]-c_rate*dist[k[1]][item])  ## c_now -> Charge Now
                if c_now<0:
                    continue  ## If the charge is not sufficient for reaching a state then discard
                else:
                    t_now=(k[0]+dist[k[1]][item]/speed)
                    heapq.heappush(q,(t_now,item,c_now)) ## Append without charging till full
                    if c_now!=capacity:
                        t_now+=(capacity-c_now)/c_rate
                        heapq.heappush(q,(t_now,item,capacity)) ## Append with charging till full
                         
    min_time = k[0] ## Minimum Time 
    return min_time, path

def mafp (ev,arr,dist):
    ''' Returns the Maximum among times taken to reach to the destination for each of the EV
    
        Parameters:
            ev = A list containing the specifications of each EV
            
        Returns:
            Maximum of Times required for EVs to reach to their Destination
    '''
    this=[]
    paths=[]
    for i in range(len(arr)):
        k=min_time(ev[i],arr,dist)
        this.append(k[0])
        paths.append(k[1])
    num=0
    for num in range(len(arr)):
        z=[]
        for i in range(len(paths)):
            z.append(paths[i][num])
        
    return max(this) ## Maximum of times required to reach the Destination for N EVs

if __name__=='__main__':
    print ('Enter the Number of EVs')
    k=int(input())
    ev=[]
    for _ in range(k):
        a=list(map(int,input().split()))
        ev.append(tuple(a))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




