class People(object):
    def __init__(self, name, dark_side=False):
        self.name = name
        self.dark_side = dark_side
        
        if not self.dark_side:
            self.light_side = True
        else:
            self.light_side = False    
   
    def __str__(self):
        return str(self.name)

    def __call__(self):
        return f"Help me {self.name}, you're my only hope."

    def __truediv__(self, opponent):
        if not isinstance(opponent, People):
            raise TypeError
        return f"{self.name} swings a lightsaber at {opponent.name}."

    def __mul__(self, opponent):
        if not isinstance(opponent, People):
            raise TypeError
        return f"{self.name} throws a thermal detonator at {opponent.name}!"        

    def __rshift__(self, opponent):
        if not isinstance(opponent, People):
            raise TypeError
        return f"{self.name} uses the force to push {opponent.name} away from them."  
    
    def __lshift__(self, opponent):
        return f"{self.name} uses the force to pull {opponent.name} towards them."  

    def __neg__(self):
        self.dark_side = True
        self.light_side = False

    def __pos__(self):
        self.dark_side = False
        self.light_side = True

    def __invert__(self):
        if self.light_side:
            self.light_side = False
            self.dark_side = True 
        elif self.dark_side:
            self.light_side = True
            self.dark_side = False   
    
    def __xor__(self, opponent):
        return f"{self.name} force chokes {opponent.name}." 
      
    def __eq__(self, opponent):
        if self.name == 'Greedo' and opponent.name == 'Han Solo':
            return (f"{opponent.name} shoots {self.name}. BECAUSE HAN SHOOTS FIRST.")
        else: 
            return (f"{self.name} shoots {opponent.name}.")



    