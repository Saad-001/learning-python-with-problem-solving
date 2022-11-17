"""
6. Answer without running the code, run in your brain.
What is the result of executing the following code? 
def dp ( l1 , l2 ) : 
    def p ( ll1 , ll2 , n ) : 
        return ll1[n] * ll2[n] 
    r = 0 
    for i in range ( len ( l1 ) ) : 
      r += p ( l1 , l2 , i ) 
    return r 


print dp ( [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] )

"""

# ans is 32
