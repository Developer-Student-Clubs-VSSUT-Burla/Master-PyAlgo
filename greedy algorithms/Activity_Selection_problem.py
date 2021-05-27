"""
Author : Robin Singh
Implementation Of Activity Selection Problem Using Greedy Approch
here we have n activities with their start and finish times. Select the maximum number of activities
that can be performed by a single person, assuming that a person can only work on a single activity at a time
Time Complexity :
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


# Entre Range Of Activities4                                                                                              
# 1.Entre  Activity       2.Exit                                                                                          
# Entre Choice1                                                                                                         Entre Start value And finish Value                                                                                      
# Start ?5                                                                                                               
# finish ?9                                                                                                               Entre Start value And finish Value                                                                                      
# Start ?1                                                                                                                finish ?6                                                                                                               Entre Start value And finish Value                                                                                      
# Start ?1                                                                                                                finish ?9                                                                                                               Entre Start value And finish Value                                                                                      
# Start ?5                                                                                                                finish ?8                                                                                                               Following Activities Are selected :                                                                                     
# Index   Start Finish                                                                                                  0             5-->9                                                                                                
# 1.Entre  Activity       2.Exit 