def write_to_file(file_name, data):
    file = open(file_name,"w") 
    file.write(data)
    file.close() 
