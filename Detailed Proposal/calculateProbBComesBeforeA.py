# Probability that string A preceds string B

import pdb

def calculateProbability(A, B):
	def starOperation(A, B):
		binaryRepresentation = [0] * len(A)

		for i in range(len(A)):
			n = len(A) 

			if  A[i: n] == B[0: n-i]:
				binaryRepresentation[i] = 1

		return binaryRepresentation

	def toDecimal(binaryRepresentation):
		decimal = 0

		for i in range(len(binaryRepresentation)):
			index = len(binaryRepresentation) - i - 1
			decimal += binaryRepresentation[index] * 2**i

		return decimal

	pdb.set_trace()

	AA = float(toDecimal(starOperation(A, A)))
	BB = float(toDecimal(starOperation(B, B))) 
	AB = float(toDecimal(starOperation(A, B))) 
	BA = float(toDecimal(starOperation(B, A)))  

	print AA

	# This is the odds a will precede B
	odds = (AA - AB) / (BB - BA)
	return 1.0/(odds + 1.0)


A = "HHH"
B = "THH"

print A, B
print calculateProbability(A, B)