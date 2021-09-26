Encrypy Bot® 
©Copyrights reserved to team De-coders

v1.0
10 July 2021

Team: Pranav Todkar, Anikate Kumar, Diya Bhagat

Project files:
1. main_code.py - Double-click the "main_code.py" file to start encrypting. (main file)
2. cipher_matrix - handles all the matrix conversion and multiplication operations.
3. readme.txt - basic info of the bot contain error info for user
4. test.txt - file that can be encrypted, and then decrypted only by the user using secure PIN.

-----------
1. Summary
-----------

 This bot provides secure transfer of files from one device to other, where someone who can intercept your file
 cannot access file contents by any means. The file can be decrypted only by using the unique 4 digit PIN.

 We highly value your privacy and security and so we do not keep any means, for even ourselves to read/retrieve your data.

 Hope you never find issue to keep your data safe. Double-click the "main_code.py" file to start encrypting! Happy encrypting :).

 The method used to encrypt/decrypt:
  Hill Cipher: Cryptography that convert normal text to encrypted test, 
  which is secured by using a key matrix with help of matrix operations. 
  For more details on working of Hill Cipher visit: https://en.wikipedia.org/wiki/Hill_cipher

 It  takes plain text from given text file and an encryption key as an input and
 produces an encrypted text. The encrypted text can be converted to plain text only if you have the 
 encryption key. Matrix operations are undertaken according to hill cipher algorithm for encrypting and decrypting text.

---------
2. Errors
---------
i. Please type only in E or D.
   <E/D> symbol: Bot accepts only these two strings (E or D).

ii. Please remember to add file extension also.
    Eg. file_name.txt

iii. Please type only in Y or N.
     <Y/N> symbol: Bot accepts only these two strings (E or D).

iv. Enter 4 digits which satisfy "ad - bc > 0"!
    Eg. 9119
    [abcd]- a,b,c,d implies only single digits.
    For more details please refer to Help section.

v. Please enter digits only!
   Please do not enter strings only digits expected.

-------
3. Help
-------
Condition for PIN:
 ad - bc > 0 (Determinant):
  Consider a 4 digit number abcd, here:
  a * d - b * c must be positive.

Relative or absolute path (relative or absolute path of file):
  Eg. Absolute path: C:\Users\Admin\Desktop\New Folder\text_file
  Location of the text file in the computer.

  Eg. Relative path: text_file
  Location of the text file with respect to the executable file.


------------------
4. Special Thanks
------------------
Thanks to Clint George sir and all the teaching assistance of CS101 for constant guidance 
and support and giving us the opportunity to create our first program based on a real life problem.
