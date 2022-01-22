#Solution of the ComputerWomen challenge for FemHack by Nuwe
#Author: Rocio Gonzalez Toral / chio.gonzalezt@gmail.com

import math
import sys
import json

g=9.807

#Compute the maximum height of the projectile (h_max)
def maximum_height(vi):
    h_max = ( vi * vi ) / ( 2 * g )
    return h_max

#Compute the maximum traveled distance
def maximum_traveled(vi, alph):
    x_max = 2 * vi* math.sin(alph) / g
    return x_max

#Save the computed data (Inputs + Results) into a file
def save_data(d1, d2, r1, r2):
    try:
        f = open ("results.txt","w")
        f.write("|Inputs:") 
        f.write(" Initial velocity: " + str(d1))
        f.write(", Launch angle: " + str(d2))
        f.write("| Results:")
        f.write(" Maximum height of the projectile: " + str(r1))
        f.write(", Maximum traveled distance: " + str(r2))
        f.write("|")
        f.close()
        print("Inputs and Results are saved in results.txt")
    except:
        print("Something go wrong with save file")
        sys.exit(1)

#Create a Json File with input data
def input_json():
    # Data to be written
    dictionary = {
        "v0" : 1.0,
        "alpha" : 30.0,
    }
    with open("inputdata.json", "w") as outfile:
        json.dump(dictionary, outfile)


#Introduction data
option = int(input("Select the way to introduce the data (1:JSON/2:Manual)"))
if (option == 1):
    #JSON
    #read from json
    nameJson=str(input("Name the Json file: "))
    # Opening JSON file
    f = open(nameJson,'r')
    # returns JSON object as a dictionary
    data = json.load(f)
    v0=data['v0']
    alpha=data['alpha']
    # Closing file
    f.close()
elif (option == 2):
    #manual
    v0=float(input("Initial velocity: "))
    alpha=float(input("Launch angle: "))
else:
    print("Just 1 or 2 option")
    sys.exit(1)
fileresult=str(input("Do you want save the results in a file(s/n)?: "))

if fileresult=="s" or fileresult=="S":
    save_data(v0,alpha,maximum_height(v0),maximum_traveled(v0,alpha))
else:
    print(f"The Maximum height of the projectile: " + str(maximum_height(v0)))
    print(f"Maximum traveled distance: " + str(maximum_traveled(v0,alpha)))


