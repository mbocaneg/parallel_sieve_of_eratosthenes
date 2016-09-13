from multiprocessing import Pool,RawArray
import ctypes,time

shared_Array=RawArray(ctypes.c_int,[1]*100000) 		#array holding prime numbers, that will be shared amongst all processes 
mult=RawArray(ctypes.c_int,[0]*1)              		#one element array, that will represent the current multiple which will
					       		#be eliminated from the prime list

chunk_List=[]                                  		#List that will contain the start/end indices for all chunks

def init(): 				       		#function that simply sets 0th and first element to 0
	shared_Array[0]=0
	shared_Array[1]=0
	
def print_shared_Array(): 		       		#function that prints out shared array, for debugging purposes
	for i in shared_Array:
		print(i)

def printPrimes():			       		#function that prints out a list of primes, for debugging purposes
	for i in range(len(shared_Array)):
		if shared_Array[i]==1:
			print(i)

def wrap(args):                                		#wrapper function used for the sole purposes of applying map to a function 						       		#that takes multiple arguments
	return sieve(*args)

def chunk(chunk_size): 			       		#function that builds a list of start/end indices based on the chunk size   								#and shared array's length
	num_chunk=int(len(shared_Array)/chunk_size)	#find number of chunks
	count=0
	start=0
	while(count<num_chunk):
		end=start+chunk_size-1	       		#calculate end index
		chunk_List.append([(start,end)])	#append start/end index to chunk list
		start=start+chunk_size	       		#move start index over
		end=end+chunk_size	       		#move end index over
		count+=1		       		#increment counter

def sieve(start,end): 			       		#function that marks primes on the shared array
	k=mult[0]
	while(start<=end):		       		#as long as start index < end index	
		if start==k and shared_Array[k]==1:	#if current multiple equals start index, and it is prime, skip
			pass			   
		elif start%k==0 :	       		#if start index divisible by current multiple,set to non-prime
			shared_Array[start]=0
		start+=1		       		#increment start index

def start(procs,chunksize): 		       		#process sieve with given worker processes and chunk size
	start=time.time()		       		#start the clock
	init()	
	chunk(chunksize)		       		#calculate chunk list
	pool=Pool(processes=procs)	       		#start process pool
	for i in range(2,int(len(shared_Array)**.5)+1):	#apply starmap to wrap function to invoke sieve(BECAUSE map DOESNT LIKE
					       		#MULTIPLE ARGUMENT FUNCTIONS!!!) for each each start/end index in chunk list
		mult[0]=i
		pool.starmap(wrap,[i for i in chunk_List])
	end = time.time()		       		#stop the clock
	par_delta = 1000*(end-start)	       		#calculate time in milliseconds, print it it out
	print('(PAR) Elapsed: {:0.1f} ms'.\
			format(par_delta) )


def main():						#main function
	pool=int(input('Please enter your pool size\n'))#prompt user for pool and chunk size
	chunk=int(input('Please enter a chunk size\n'))
	start(pool,chunk)
	
	print_primes=(input('Print out primes? Y/N\n')) #OPTIONAL -print out a list of generated prime numbers
	if(print_primes.lower() == "y"):
	 printPrimes()
	elif (print_primes.lower() == "n"):
	 pass
main()				       		







