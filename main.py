class Grammar:

    def __init__(self):
        self.start = None
        self.products = {}
    
    def read_from_file(self):

        from tkinter import Tk
        from tkinter.filedialog import askopenfilename

        # read the input file   
        root = Tk()
        # we don't want a full GUI, so keep the root window from appearing
        root.withdraw() 
        # move the window in focus
        root.lift()
        root.attributes("-topmost", True)
        # file asking
        filename = askopenfilename(filetypes=(('Text files', '*.txt'),)) # show an "Open" dialog box and return the path to the selected file
        
        if filename == '':
            print("No file selected!")
            return
        else:
            file = open(filename, encoding='utf-8')
            
            for line in file.readlines():
                
                # get the nonterminating char
                left = line.split(" -> ")[0]

                # get the products
                products = "".join(line.split(" -> ")[1]).strip().split(" | ")
                products = [[letter for letter in word] for word in products]

                self.products[left] = products

                # set the start
                if self.start == None:
                    self.start = left

    def display_products(self):
        for key in self.products:
            print(key, self.products[key])

    def verify_word(self, word, current_symbol = None, results = []):
        

        # default case from start
        if current_symbol == None:
            current_symbol = self.start

        print(current_symbol, end=' -> ')
        
        # if we parsed the whole word and we have 
        # a lambda exit - we validated the word
        if len(word) == 0 and ['λ'] in self.products[current_symbol]:
            results.append(True)
            return True
        
        for letter in self.products[current_symbol]:

            # right linear grammar
            if word and word[0] == letter[0] and letter[0].islower():
                if self.verify_word(word[1:], letter[1]):
                    return True
            
            # left linear grammar
            elif letter[0].isupper():
                if self.verify_word(letter[1] + word, letter[0]):
                    return True
        
        
        results.append(False)
        print(results)
        return False
            
x = Grammar()
x.read_from_file()
x.display_products()
print(x.verify_word('d'))