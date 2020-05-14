with open("welcome.txt") as text_file:
  text_data = text_file.read()
  print(text_data)
  
with open("welcome.txt") as text_file:
  text_data_1 = text_file.readlines()
  print(text_data_1)
  
# work better with lengthy text by approaching one line at a time
with open("how_many_lines.txt") as lines_doc:
  for line in lines_doc.readlines():
    print(line)
# work faster with short text 
with open("how_many_lines.txt") as lines_doc:
    for line in lines_doc:
        print(line)