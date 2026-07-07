
def ChkNum(No) :

	if(No>0) :
		print("Positive Number.")
	elif(No<0) :
		print("Negative Number.")
	else :
		print("Zero.")
		
def main() :

	print("Enter Number :")
	No = int(input())

	ChkNum(No)

		
if __name__ == "__main__" :
	main()
	
'''
OUTPUT:
1.Enter Number :
  11
  Positive Number.

2.Enter Number :
  -8
  Negative Number.

3.Enter Number :
  0
  Zero.
'''