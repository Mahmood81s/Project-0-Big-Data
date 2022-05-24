
import json

# opening JSON file
f = open(r'C:\Users\mahmo\project_zero_cli\col_movie_3.json')  # opening JSON file

#returns JSONobject as a dictionary
data = json.load(f)

# iterating through the json list 
for i in data['col_movie_3']:
    print(i)
    
#closing file 
f.close() 