# Reading a File
with open("welcome.txt") as text_file:
  text_data = text_file.read()
  print(text_data)
  
with open("welcome.txt") as text_file:
  text_data_1 = text_file.readlines()
  print(text_data_1)
  
# Iterating Through Lines
# work better with lengthy text by approaching one line at a time
with open("how_many_lines.txt") as lines_doc:
  for line in lines_doc.readlines():
    print(line)
# work faster with short text 
with open("how_many_lines.txt") as lines_doc:
    for line in lines_doc:
        print(line)
        
        
# Reading a Line      
with open("just_the_first.txt") as first_line_doc:
  first_line = first_line_doc.readline()
  first_line1 = first_line_doc.readline()
  print(first_line)
  print(first_line1)
  
# Writing a File 
# Will create a new file with the given name, if there is a file exist ==> overwrite content 
with open("bad_bands.txt", "w") as bad_bands_doc:
   bad_bands = bad_bands_doc.write("HKT Band")