def output_cats_and_dogs(filename):    
        try:
            with open(filename) as f: 
                contents = f.read()            
        except FileNotFoundError:
            print(f"\nFile {filename} wasn't found")
        else:
            print(f"\nNames:\n{contents}")


files = ["chapter10\exercises\cats.txt", "chapter10\exercises\dogs.txt"]
for file in files:
    output_cats_and_dogs(file)    

