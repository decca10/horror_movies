class conf_mat:
    """
    Method to pass in a confusion matrix and spit out interpretation results.
    """
    def __init__(self,tn,fp,fn,tp):
        self.tn = tn 
        self.fp = fp
        self.fn = fn
        self.tp = tp 

    def sens(self):
        """
        How many true positives did I predict?
        (no p's in the word, so all p's in the math)
        """
        print(f'Sensitivity is {self.tp / (self.tp + self.fn)}')

    def spec(self):
        """
        How many true negatives did I predict?
        (all p's in the word, so no p's in the math)
        """
        print(f'Specificity is {self.tn / (self.tn + self.fp)}')

    def prec(self):
        """
        How many corret positive predictions did I get?
        (lots of p's in word and description = all p's in the math)
        """
        print(f'Precision is {self.tp / (self.tp + self.fp)}')

    def acc(self):
        """
        How many actuals did I get right?
        """
        print(f'Accuracy is {(self.tp + self.tn) / (self.tn + self.fp + self.fn + self.tp)}')

    def misc(self):
        """
        How many predictions did I get wrong?
        """
        print(f'Misclassification Rate is {1 - ((self.tp + self.tn) / (self.tn + self.fp + self.fn + self.tp))}')

    def all(self):
        print(f'Sensitivity is {self.tp / (self.tp + self.fn)}')
        print(f'Specificity is {self.tn / (self.tn + self.fp)}')
        print(f'Precision is {self.tp / (self.tp + self.fp)}')
        print(f'Accuracy is {(self.tp + self.tn) / (self.tn + self.fp + self.fn + self.tp)}')
        print(f'Misclassification Rate is {1 - ((self.tp + self.tn) / (self.tn + self.fp + self.fn + self.tp))}')
        
        
        
        

