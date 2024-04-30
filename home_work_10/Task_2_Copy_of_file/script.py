with open("some content.txt", "w") as file:
   content  = file.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
                          sed do eiusmod tempor incididunt ut labore et dolore magna aliqua")
   
with open("some content.txt", "r") as file:
      file_to_copy = file.read()
      with open("copy_of_content.txt", "w") as file_2:
         copy_of_content = file_2.write(file_to_copy.upper())

    