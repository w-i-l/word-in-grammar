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

                if left in self.products:
                    self.products[left].extend(products)
                else:
                    self.products[left] = products

                # set the start
                if self.start == None:
                    self.start = left

    def display_products(self):
        for key in self.products:
            print(key, self.products[key])

    def verify_word(self, word, current_symbol = None):
        

        # default case from start
        if current_symbol == None:
            current_symbol = self.start

        
        # if we parsed the whole word and we have 
        # a lambda exit - we validated the word
        if (len(word) == 0 or word == 'λ') and ['λ'] in self.products[current_symbol] :\
            # or len(word) == 1 and [word] in self.products[current_symbol]:
            print(current_symbol, end=' -> ')

            return True
        
        for letter in self.products[current_symbol]:

            # right linear grammar
            if word and word[0] == letter[0] and letter[0].islower():

                # only a terminal
                if len(letter) == 1:
                    return True

                elif self.verify_word(word[1:], letter[1]):
                    
                    print(current_symbol, end=' -> ')
                    return True
            
            # left linear grammar
            elif letter[0].isupper():
                if self.verify_word(letter[1] + word, letter[0]):
                    
                    print(current_symbol, end=' -> ')
                    return True
        
        return False
    

if __name__ == '__main__':
    x = Grammar()
    x.read_from_file()
    # x.display_products()

    while True:

        print("\nPress q to exit")
        word = input("Enter a word: ")
        
        if word == 'q':
            break

        print(f"Choosen word: {word}")
        print('Result: ', x.verify_word(word))