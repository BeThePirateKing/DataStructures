class Trie:
    root = None
    count = 0
    def __init__(self, letter=None):
        if count == 0:
            root = self
            self.alphabet = None
        count+= 1
        self.word = None
        self.alphabet = letter
        self.child = []
        self.noOfWords = 1
        self.isTerminal = False

    def setTerminal(self):
        self.isTerminal = True
    
    def setWord(self, word):
        self.word = word

    def getWord(self):
        return self.word
    
    def getAlphabet(self):
        return self.alphabet

    def addChild(self, new):
        self.child.append(new)

    def getLetter(self):
        return self.letter

    def searchChild(self, letter):
        found = False
        for child in self.child:
            if child.getAlphabet() == letter:
                found = True
                return child
        if not found:
            return 0

    def insert(self, word, pos=0):
        letter = word[pos]
        child = self.searchChild(letter)
        if child:
            if len(word) == pos+1:
                child.setTerminal()
                child.setWord(word)
            else:
                pos+=1
                child.insert(word, pos)

        else:
            new = Trie(letter)
            self.addChild(new)
            if len(word) == pos+1:
                new.setTerminal()
                new.setWord(word)
            else:
                pos+=1
                new.insert(word,pos)
    
    def getAllWords(self):
        words = []
        if len(self.child) == 0:
            return [self.getWord()] 
        else:
            for child in self.child:
                word = child.getAllWords()
                for w in word:
                    words.append(w)
                if child.isTerminal:
                    words.append(child.getWord())
            words.sort()
            return words


    def autoComplete(self, prefix, pos=0):
        letter = prefix[pos]
        if len(prefix) == pos+1:
            suffixes = self.getAllWords()
            return suffixes
        else:
            child = self.searchChild(letter)
            if child:
                pos+=1
                return child.autoComplete(prefix, pos)
            else:
                return []
            

    def getEveryWord(self):
        return root.getAllWords()

    def getNoOfWords(self):
        return count

        



            
    

    
