#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


class sorting_algo:
    
    
    def __init__(self, arr, n):
        self.arr = arr
        self.n = n
        
    def swap (self, i, j):
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = temp
        
        
    ####### SELECTION SORT #######
        
    def selection_sort(self):
        for i in range(0,self.n-1):
            min = i
            for j in range(i+1,self.n):
                if(self.arr[min]>self.arr[j]):
                    min = j
            self.swap(i,min)
            
            
    ####### BUBBLE SORT #######
            
            
    def bubble_sort(self):
        for i in range(0,self.n-1):
            for j in range(0,self.n-i-1):
                if(self.arr[j]>self.arr[j+1]):
                    self.swap(j,j+1)
                    
                    
    def bubble_sort_optimized(self):
        for i in range(0,self.n-1):
            swap = False
            for j in range(0,self.n-i-1):
                if(self.arr[j]>self.arr[j+1]):
                    swap = True
                    self.swap(j,j+1)
            if(swap == False):
                break
    
    
    ####### INSERTION SORT #######
    
    def insertion_sort(self):
        for i in range(1,self.n):
            temp = self.arr[i]
            ind = i
            for j in range(i-1,-1,-1):
                if(self.arr[j]>temp):
                    self.arr[j+1] = self.arr[j]
                    ind = j
                else: break
            self.arr[ind] = temp
            
            
            
    ####### MERGE SORT #######
            
            
    def merge(self, l, mid, r):
        i,j= l,mid+1
        new_arr = []
        while(i<=mid and j<=r):
            if(self.arr[j]<self.arr[i]):
                new_arr.append(self.arr[j])
                j+=1
            else:
                new_arr.append(self.arr[i])
                i+=1
        while(i<=mid):
            new_arr.append(self.arr[i])
            i+=1
        while(j<=r):
            new_arr.append(self.arr[j])
            j+=1
        for k in range(0, len(new_arr)):
            self.arr[l] = new_arr[k]
            l+=1
            
    
    def merge_sort(self,l,r):
        if(l==r): return
        mid = l+(r-l)//2
        self.merge_sort(l,mid)
        self.merge_sort(mid+1,r)
        self.merge(l,mid,r)
        
        
        
    ####### QUICK SORT #######
        
    def partition(self,l,r):
        i, pivot = l,r
        if(self.arr[i]<=self.arr[pivot]):
            i+=1
        for j in range(l+1,r):
            if(self.arr[j]<=self.arr[pivot]):
                self.swap(i,j)
                i+=1
        self.swap(pivot,i)
        return i

    
    def randomized_partition(self,l,r):
        ran = l + (random.randint(l,r))%(r-l+1)
        self.swap(ran,r)
        return self.partition(l,r)
    
    
    def quick_sort(self, l, r):
        if(l>=r): return
        pivot = self.randomized_partition(l,r)
        self.quick_sort(l,pivot-1)
        self.quick_sort(pivot+1,r)
    
    
    
    ####### COUNTING SORT #######
    
    def counting_sort(self):
        max_num = max(self.arr)
        freq_arr = [0]*(max_num+1)
        new_arr = [0] * self.n
        for i in range(self.n):
            freq_arr[self.arr[i]]+=1    
        for i in range(1,len(freq_arr)):
            freq_arr[i] +=freq_arr[i-1]
        for i in range(self.n-1,-1,-1):
            ind = self.arr[i]
            freq_arr[ind]-=1
            new_arr[freq_arr[ind]] = ind
        for i in range(self.n):
            self.arr[i] = new_arr[i]
            
            
            
    ####### RADIX SORT #######
            
     
    def counting_sort_subroutine_for_radix_sort(self, dig):
        freq_arr = [0]*(10)
        new_arr = [0] * self.n
        for i in range(self.n):
            freq_arr[(self.arr[i]%(dig*10))//dig]+=1    
        for i in range(1,len(freq_arr)):
            freq_arr[i] +=freq_arr[i-1]
        for i in range(self.n-1,-1,-1):
            ind = (self.arr[i]%(dig*10))//dig
            freq_arr[ind]-=1
            new_arr[freq_arr[ind]] = self.arr[i]
        for i in range(self.n):
            self.arr[i] = new_arr[i]
    
    def radix_sort(self):
        max_num = max(self.arr)
        i = 1
        while(max_num//i>0):
            self.counting_sort_subroutine_for_radix_sort(i)
            i*=10
    
    
    def print_array(self):
        print("The elements of the array after sorting is:")
        for i in range(self.n):
            print(self.arr[i], end = " ")
        print()
    
def main():
    
    print("Enter the number of elements of the input array:")
    n = int(input())
    
    arr = []
    print("\nEnter the elements of the array:")
    for i in range(n):
        arr.append(int(input()))
        
    sa = sorting_algo(arr,n)
    
    print("\n## SELECTION SORT ##")
    sa.selection_sort()
    sa.print_array()
    random.shuffle(arr)
    
    print("\n## BUBBLE SORT ##")
    sa.bubble_sort()
    sa.print_array()
    random.shuffle(arr)
    
    print("\n## BUBBLE SORT OPTIMIZED ##")
    sa.bubble_sort_optimized()
    sa.print_array()
    random.shuffle(arr)
    
    print("\n## INSERTION SORT ##")
    sa.insertion_sort()
    sa.print_array()
    random.shuffle(arr)
    
    print("\n## MERGE SORT ##")
    sa.merge_sort(0,n-1)
    sa.print_array()
    random.shuffle(arr)
    
    print("\n## QUICK SORT ##")
    sa.quick_sort(0,n-1)
    sa.print_array()
    random.shuffle(arr)
    
    print("\n## COUNTING SORT ##")
    sa.counting_sort()
    sa.print_array()
    random.shuffle(arr)
    
    print("\n## RADIX SORT ##")
    sa.radix_sort()
    sa.print_array()
        

if __name__ == "__main__":
    main()


# In[ ]:




