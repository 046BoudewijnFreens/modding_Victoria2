import re

my_file = open("Brazil.txt")
string_list = my_file.readlines()
my_file.close()

for i in range(len(string_list)): #Go trough all the different lines in the .txt file
    next_line = False
    for character in string_list[i]:
        if character.isdigit() and next_line == False and ("size =" in string_list[i] or "size=" in string_list[i]):
            initial_population = re.findall('[0-9]+', string_list[i]) #What is the original population
            new_population= round(16* int(initial_population[0]))# Calculate the appropriate new population
            #print(new_population)
            #print(str(initial_population[0]))
            print(string_list[i])
            fin = open("Brazil.txt", "rt") #replace the old population with the new one
            data = fin.read()
            data = data.replace(str(string_list[i]), "size = "+str(new_population))
            fin.close()
            fin = open("Brazil.txt", "wt")
            fin.write(data)
            fin.close()

            next_line = True #Once the initial population has been replaced with the new one, go to the next line
