# Function to demonstrate the number of moves to shift rings from start rod to end rod 
def Tower_of_Hanoi(num , start_rod, end_rod, aux_rod):
    if(num == 1):
        print("Move disk 1 from",start_rod,"to",end_rod)
    else:
        Tower_of_Hanoi(num-1, start_rod, aux_rod, end_rod)
        print("Move disk",num,"from",start_rod,"to",end_rod)
        Tower_of_Hanoi(num-1, aux_rod, end_rod, start_rod)

if __name__ == "__main__" :       
    num=int(input("Enter the number of rings in the first rod:"));
    Tower_of_Hanoi(num,'A','C','B');
    
'''
Enter the number of rings in the first rod:3
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
'''

