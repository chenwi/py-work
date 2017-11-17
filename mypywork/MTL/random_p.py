# Generate random predictions

from random import seed
from random import randrange

def random_algorithm ( train, test ) :

    output_values = [ row [ -1 ] for row in train ]
    unique = list ( set ( output_values ) )
    predicted = list ( )

    # print (output_values,unique,predicted)

    for row in test:
        index = randrange (len ( unique ) )
        predicted.append ( unique [ index ] )

    print (output_values, unique, predicted)

    return predicted



seed( 10)
train = [ [ 0 ] , [ 1 ] , [ 0 ] , [ 1 ] , [ 0 ] , [ 1 ] ]
test = [ [ None ] , [ None ] , [ None ] , [ None ] ]
predictions = random_algorithm ( train, test )



print( predictions )