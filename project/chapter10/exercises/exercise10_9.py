def output_cats_and_dogs(filename):    
        try:
            with open(filename) as f: 
                contents = f.read()            
        except FileNotFoundError:
            pass
        else:
            print(f"\nNames:\n{contents}")


files = ["chapter10\exercises\cats.txt", "chapter10\exercises\dogs1.txt"]
for file in files:
    output_cats_and_dogs(file)    

