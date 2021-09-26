import cipher_matrix as M

# Greeting for consumer

print()
print()
print('                   Welcome to Encrypy Bot')
print('===========================================================')
print('                Secure your files at one go.')
print()
print()

#/ Greeting for consumer

# A continuous loop to encrypt one file after other.

while (True):
  
  # Start with asking for encryption or decryption.

  purpose = input("Do you want to encrypt or decrypt <E/D>: ")

  #/ Start with asking for encryption or decryption.
  
  while (purpose != "E" and purpose != "D"):
    print("Error: '"+purpose+"' is not a valid response!!!!!")
    print("Please type only in E or D.")
    print()
    purpose = input("Do you want to encrypt or decrypt <E/D>: ")
  
  
  if purpose == "E":

    '''
    Loop for encrypting the TEXT file.
    '''

    # Read text from the text file.

    while (True):
      try:
        fil = input("Enter relative or absolute path of file: ")
        fo = open(fil)
        text = fo.read()
        fo.close()
        break
      except:
        print("Error: '"+fil+"' file not found!!!!!")
        print("Please remember to add file extension also.")
        print()

    #/ Read text from the text file.


    # Application of Hill Cipher:

    # Creating default KEY.

    key_matrix  = [[1 , 1], [1 , 6]]
    
    print()
    print('Default PIN is = 1116')
    print()

    #/ Creating default KEY.

    plain_text = text

    ask = input("Do you want to create your own PIN <Y/N>: ")

    while (ask != "Y" and ask != "N"):
        print("Error: '"+ask+"' is not a valid response!!!!!")
        print("Please type only in Y or N.")
        print()
        ask = input("Do you want to create your own PIN <Y/N>: ")

    # Taking and setting custom KEY.

    if ask == "Y":
      
      key = input("Enter a four-digit PIN [abcd] which has \"ad - bc > 0\": ")

      while (True):
        try:
          assert len(key)== 4
          determinant = int(key[0]) * int(key[3]) - int(key[1]) * int(key[2])
          assert determinant > 0
          break
        except ValueError as not_int:
          print("Error: '"+key+"' is not a valid PIN!!!!!")
          print("Please enter digits only!")
          print()
          key = input("Enter a four-digit PIN [abcd] which has \"ad - bc > 0\": ")
        except AssertionError as false:
          print("Error: '"+key+"' is not a valid PIN!!!!!")
          print("Enter 4 digits which satisfy \"ad - bc > 0\"!")
          print()
          key = input("Enter a four-digit PIN [abcd] which has \"ad - bc > 0\": ")

      key_matrix = [[ int(key[0]) , int(key[1]) ], [ int(key[2]) , int(key[3]) ]]

      #/ Taking and setting custom KEY.
      
    else: # Use default KEY if user doesn't want to set custom KEY
      key_matrix = key_matrix
    
    # Making matrix of text to compute

    plain_text_matrix = M.text_TO_text_matrix(plain_text)

    #/ Making matrix of text to compute

    # Getting final Encrypted text

    encrypted_text = M.matrix_multiplication(key_matrix, plain_text_matrix)

    #/ Getting final Encrypted text

    #/ Application of Hill Cipher.

    # Writing encrypted text back in the file

    if (len(plain_text) % 2 ==0):
      final_print = (encrypted_text)
    else:
      final_print = (encrypted_text + plain_text[len(plain_text) - 1])
    
    fw = open(fil, mode= 'w')
    fw.write(final_print)
    fw.close()

    #/ Writing encrypted text back in the file

    # Message to user: Encryption complete

    print()
    print()
    print("Your file has succesfully encrypted!")
    print()
    print("CAUTION: Please do remember the key \""+ key + "\" to decrypt this file.")
    print()

    #/ Message to user: Encryption complete
    
    # Continue with other files
    continue_or_not = input("Continue to encrypt or decrypt some more files? <Y/N>: ")

    while (continue_or_not != "Y" and continue_or_not != "N"):
      print("Error: '"+ continue_or_not+"' is not a valid response!!!!!")
      print("Please type only Y or N.")
      print()
      continue_or_not = input("Continue to encrypt or decrypt some more files? <Y/N>: ")

    if (continue_or_not =="Y"):
      continue
    else:
      break
    #/ Continue with other files

    '''
    <END> Loop for encrypting the TEXT file.
    '''





  
  else:

    '''
    Loop for DEcrypting the TEXT file.
    '''

    # Read text from the text file.
    while (True):
      try:
        fil = input("Enter relative or absolute path of file: ")
        fo = open(fil)
        text = fo.read()
        fo.close()
        break
      except:
        print("Error: '"+fil+"' file not found!!!!!")
        print("Please remember to add file extension also.")
        print()
    #/ Read text from the text file.

    # Applcation of Hill Cipher:

    # Creating default KEY.

    key_matrix  = [[1 , 1], [1 , 6]]

    print()
    print('Default PIN is = 1116')
    print()
    #/ Creating default KEY.

    encrypted_text = text

    ask = input("Do you have your own PIN <Y/N>: ")
    
    while (ask != "Y" and ask != "N"):
      print("Error: '"+ask+"' is not a valid response!!!!!")
      print("Please type only in Y or N.")
      print()
      ask = input("Do you have your own PIN <Y/N>: ")
    
    # Taking and setting custom KEY.
    if ask == "Y":

      key = input("Enter the four-digit PIN [abcd] which has \"ad - bc > 0\": ")

      while (True):
        try:
          assert len(key)== 4
          determinant = int(key[0]) * int(key[3]) - int(key[1]) * int(key[2])
          assert determinant > 0
          break
        except ValueError as not_int:
          print("Error: '"+key+"' is not a valid PIN!!!!!")
          print("Please enter digits only!")
          print()
          key = input("Enter a four-digit PIN [abcd] which has \"ad - bc > 0\": ")
        except AssertionError as false:
          print("Error: '"+key+"' is not a valid PIN!!!!!")
          print("Enter 4 digits which satisfy \"ad - bc > 0\"!")
          print()
          key = input("Enter a four-digit PIN [abcd] which has \"ad - bc > 0\": ")
        
      key_matrix = [[ int(key[0]) , int(key[1]) ], [ int(key[2]) , int(key[3]) ]]

      #/ Taking and setting custom KEY.
    
    else: # Use default KEY if user doesn't want to set custom KEY
      key_matrix = key_matrix

    # Making KEY INVERSE MATRIX

    key_inverse_matrix = M.key_matrix_TO_key_inverse_matrix(key_matrix)

    #/ Making KEY INVERSE MATRIX

    # Making matrix of text to compute

    encrypted_text_matrix = M.text_TO_text_matrix(encrypted_text)
    
    #/ Making matrix of text to compute

    # Getting final DEcrypted text

    plain_text = M.matrix_multiplication(key_inverse_matrix, encrypted_text_matrix)

    #/ Getting final DEcrypted text

    #/ Applcation of Hill Cipher.

    # Writing DEcrypted text back in the file
    
    if (len(encrypted_text) % 2 == 0):
      final_print = (plain_text)
    else:
      final_print = (plain_text + encrypted_text[len(encrypted_text) - 1])

    fw = open(fil, mode= 'w')
    fw.write(final_print)
    fw.close()

    #/ Writing DEcrypted text back in the file

    # Message to user: DEcryption complete

    print()
    print()
    print("Your file has succesfully decrypted!")
    print()
    print()

    #/ Message to user: DEcryption complete

    # Continue with other files
    
    continue_or_not = input("Do you want to continue <Y/N>: ")

    while (continue_or_not != "Y" and continue_or_not != "N"):
      print("Error: '"+ continue_or_not+"' is not a valid response!!!!!")
      print("Please type only Y or N.")
      print()
      continue_or_not = input("Do you want to continue <Y/N>: ")

    if (continue_or_not == "Y"):
      continue
    else:
      break
    
    #/ Continue with other files

    '''
    <END> Loop for DEcrypting the TEXT file.
    '''

#/ A continuous loop to encrypt one file after other
