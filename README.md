This is a simple project of Steganography, which includes encrypting a message into image and later decrypting using the keys.
The user inputs a message and gets an image encrypted with the message and 2 keys.
The user can then transfer this image and provide the keys to the destination.
The user at destination will then use the image and keys to input in the decryption program to retrieve the message.

Algorithm:

Encryption:
1.	The entered message is converted from string into list of characters.
2.	Each character is then converted into its respective ASCII value and stored in another list.
3.	The list is 1D which if converted to image will have only one dimension. Hence, to make it into rows and columns the list is reshaped to 2D. This is done by finding the factors of the length of message. The middle factor is taken as row count and then the column count is taken by dividing length of message by total count.
4.	If the length is a prime number, then there will be no factors other than 1 and the length itself. In that case ‘`’ is appended at the end of the message to increase the length by 1 and making it non-prime and hence now the row count will be more than 1.
5.	Now the matrix is converted into image with CV2.
6.	As the message usually will be of short length the image obtained will be tiny. So, it is resized to [500,500] to make it visible.
7.	The image is then stored and the row count and column count are provided as the keys to the user.

Decryption:
1.	Keys are taken as input.
2.	The encrypted image is read.
3.	The encrypted image which is of size [500,500] is then converted into original size of the keys [m,n].
4.	The message is then decrypted as list of characters by converting the first pixel from ASCII values to character.
5.	The list of characters is then converted to string and given as output to the user.

