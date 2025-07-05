# Open the file.
myfile = open ('numbers.txt','r')
# Read and display the file's contents. 
for line in myfile:
  number = int (line) I
  print (number)
# Close the file. 
myfile.close ()
