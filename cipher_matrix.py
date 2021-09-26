
'''

Hill cipher

'''
#Dictionary for handling all characters in a text.
#Author: Anikate
Alphabet = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25,'a':26,'b':27,'c':28,'d':29,'e':30,'f':31,'g':32,'h':33,'i':34,'j':35,'k':36,'l':37,'m':38,'n':39,'o':40,'p':41,'q':42,'r':43,'s':44,'t':45,'u':46,'v':47,'w':48,'x':49,'y':50,'z':51,' ':52,'!':53,'"':54,'#':55,'$':56,'%':57,'&':58,'\'':59,'(':60,')':61,'*':62,'+':63,',':64,'-':65,'.':66,'/':67,'0':68,'1':69,'2':70,'3':71,'4':72,'5':73,'6':74,'7':75,'8':76,'9':77,':':78,';':79,'<':80,'>':81,'=':82,'?':83,'@':84,'[':85,']':86,'\n':87,'_':88 ,"|": 89, "\\" : 90, "{": 91, "}": 92, "~": 93, "`": 94, "^" : 95, "±" : 96}

# First Function of the matrix module : text_TO_text_matrix()

#Function Author: Diya
#Doc Author: Pranav

def text_TO_text_matrix(plain_text):
  '''
  Input argument: A String

  The function takes the string text and replaces the alphabet by a unique number.

  This number is stored in a nested list.

  Ex. String = "Hi there"

  A list is created of form:
  [ [num(H), num(i)] , [num( ), num(t)] , [num(h), num(e)] , [num(r), num(e)] ]

  Its called a matrix as it can be visualised like:
  [ [num(H),] , [num( ),] , [num(h),] , [num(r),]]
     num(i)      num(t)      num(e)      num(e)
     
  Output: A list
  '''
  plain_text_matrix = []
  # [[0, 1], [2 , 3]]

  length_of_plain_text = len(plain_text)
      

  for i in range(length_of_plain_text // 2):
    plain_column_matrix = []

    a = plain_text[2 * i]
    plain_column_matrix.append(Alphabet.get(a))

    b = plain_text[2 * i + 1]
    plain_column_matrix.append(Alphabet.get(b))

    plain_text_matrix.append(plain_column_matrix)

  return plain_text_matrix

# Second Function of the matrix module : key_matrix_TO_key_inverse_matrix()

#Function Author: Anikate
#Doc Author: Anikate

def key_matrix_TO_key_inverse_matrix(key_matrix):
  '''This is a function which has one parameter.
     This parameter can only be a 2x2 key matrix.
     This function is use to find the inverse of the given key matrix only.
     Point to be noted that this inverse matrix have some adultration because of hill cipher alorithm,
     so it does not represent actual inverse.'''
  
  # Actual inverse of a 2x2 matrix
  inverse_matrix =[[key_matrix[1][1],-(key_matrix[0][1])],[-(key_matrix[1][0]),key_matrix[0][0]]]

  # To check negative elements and add 97 till we get positive value 
  for i in range(2):
    for j in range(2):
      while (inverse_matrix[i][j] < 0):                            
        inverse_matrix[i][j] += 97

  # TO check Determinant of the key inverse matrix is not to be negative.
  det = (key_matrix[1][1]*key_matrix[0][0] - key_matrix[0][1]*key_matrix[1][0]) # ad - bc > 0
    
  if (det > 0):
    det = det
  else:                                                 # If the inverse is negative then multiplying it by "-1" and make it positive.
    det *= -1

  #findind i such that (det*i) modulus with 97 is 1.
  i = 1                                                 
  while (det * i) % 97 != 1:
    i += 1
  
  # i is the factor to be multiplied to every element of key inverse matrix.
  multiplicative_inverse = i
    
  # Multipling each element of key inverse matrix by i and taking there modulus with 97 to get the hill cipher key inverse matrix.
  for i in range(2):
    for j in range(2):
      inverse_matrix[i][j] *= multiplicative_inverse
      inverse_matrix[i][j]  %= 97

  return inverse_matrix     # returning the inverse matrix when the function key_matrix_TO_key_inverse_matrix() is called.

# Third Function of the matrix module : matrix_multiplication()

#Function Author: Pranav
#Doc Author: Diya

def matrix_multiplication(key_matrix, plain_text_matrix):
  ''' 
  this function performs the matrix multiplication of key matrix and plain text matrix
           take the column module 97
           converts them back into string text corresponding to their key value from dictonary( Alphabet)
           to produce the encryped text
  '''
  
  number_of_column_matrices_in_plain_text_matrix = len(plain_text_matrix)

  # Making the Encrypted text matrix by 2*2 matrix multiplication  
  encrypted_text_matrix = [] 

  #Multiplying key_matrix with plain_text_matrix and taking their modulus with 97
  for i in range(number_of_column_matrices_in_plain_text_matrix):
    encrypted_column_matrix = []

    encrypted_column_matrix.append((key_matrix[0][0] * plain_text_matrix[i][0] + key_matrix[1][0] * plain_text_matrix[i][1]) % 97)
    encrypted_column_matrix.append((key_matrix[0][1] * plain_text_matrix[i][0] + key_matrix[1][1] * plain_text_matrix[i][1]) % 97)

    encrypted_text_matrix.append(encrypted_column_matrix)

  # Making the Encrypted text 
  encrypted_text = ""
    

  number_of_column_matrices_in_encrypted_text_matrix = len(encrypted_text_matrix)

  #generating the encryped text
  #from the encryped column matrix
  for i in range(number_of_column_matrices_in_encrypted_text_matrix):

    a = list(Alphabet.keys())[list(Alphabet.values()).index(encrypted_text_matrix[i][0])]
    encrypted_text += a

    b = list(Alphabet.keys())[list(Alphabet.values()).index(encrypted_text_matrix[i][1])]
    encrypted_text += b


  return encrypted_text    #returns the encrypted text wnen the function matrix_multiplication() is called.
