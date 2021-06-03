"""
Author : Robin Singh
Implementation Of Activity Selection Problem Using Greedy Approch
The Activity Selection Problem is an optimization problem that deals with the selection of non-conflicting activities that must be completed in a specified time frame by a single human or machine.
Each activity has a start and completion time. Because this is an optimization problem, a greedy strategy is utilised to locate the answer.
Assume you have n activities with start and finish timings; the goal is to identify a solution set with the greatest number of non-conflicting activities that can be done in a single time frame, assuming that only one human or machine is available for execution.

Here are a few things to keep in mind:
- Because their timings can collide, it is probable that not all of the activities will be completed.
- Two activities, say I and j, are said to be non-conflicting if si >= fj or sj >= fi, where si and sj signify the beginning and ending times of activities I and j, respectively, and fi and fj signify the beginning and ending times of activities I and j, respectively.
- We can adopt a greedy strategy to identify a solution since we want to maximise the number of activities that can be completed. This method will greedily select the activity with the earliest finish time at each phase, resulting in an optimal solution.

"""

def activity_selection_prob(s,f,n):
    print("Following Activities Are selected :")
    j = 0
    print("Index\tStart\tFinish")
    print(f"{j}\t\t{s[j]} -->\t{f[j]}")
    for i in range(1,n):
        if s[i]>=f[j]:
            print(f"{i}\t\t{s[i]} -->\t{f[i]}")
            j =i


if __name__ == '__main__':
    c= int(input("Entre Range Of Activities"))
    start = [0]*c
    finish = [0]*c
    while(1):
        print("1.Entre  Activity\t2.Exit")
        ch  = int(input("Entre Choice"))
        if ch == 2:
            break
        elif ch ==1:
            for i in range(0,c):
                print("Entre Start value And finish Value")
                a = int(input("Start ?"))
                b = int(input("finish ?"))
                start[i],finish[i] = a,b
            activity_selection_prob(start, finish, len(start))

        else:
            print("Invalid Option")

"""
Entre Range Of Activities4                                                                                              
1.Entre  Activity       2.Exit                                                                                          
Entre Choice1
Entre Start value And finish Value                                                                                      
Start ?5                                                                                                               
finish ?9
Entre Start value And finish Value                                                                                      
Start ?1                                                                                                                
finish ?6                                                                                                              
Entre Start value And finish Value                                                                                      
Start ?1                                                                                                                
finish ?9                                                                                                              
Entre Start value And finish Value                                                                                      
Start ?5                                                                                                                
finish ?8                                                                                                               
Following Activities Are selected :                                                                                     
Index   Start Finish                                                                                                  
0             5-->9                                                                                                
1.Entre  Activity       2.Exit 
"""