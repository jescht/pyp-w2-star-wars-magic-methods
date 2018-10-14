class SaberCrystal(object):
    def __init__(self, color=(255,0,0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]



    @property
    def color(self):
        return (self.red,self.green,self.blue)
        

    def __eq__(self,other):
        if self.color == other.color: 
            return True
        else:
            return False

    def __add__(self,other):
        if isinstance(other, tuple):
            other = SaberCrystal(color=other)
        
        rgb_values = [self.red + other.red, self.green + other.green, self.blue + other.blue]
        '''list comprehension for following expression:
        new_color = []
        for value in rgb_values: 
            if value > 255:
                value = 255
            new_color.append(value)'''        
        new_color = [255 if value > 255 else value for value in rgb_values]

        return SaberCrystal(new_color)

    def __iadd__(self,other):
        if isinstance(other, tuple):
            other = SaberCrystal(color=other)
        self.red = self.red + other.red
        self.green = self.green + other.green
        self.blue = self.blue + other.blue
        rgb_values = [self.red, self.green, self.blue]
        new_color = [255 if value > 255 else value for value in rgb_values]        
        return SaberCrystal(new_color)

    def __sub__(self,other):
        if isinstance(other, tuple):
            other = SaberCrystal(color=other)
        
        rgb_values = [self.red - other.red, self.green - other.green, self.blue - other.blue]
        new_color = [0 if value < 0 else value for value in rgb_values]       

        return SaberCrystal(new_color)

    def __isub__(self,other):
        if isinstance(other, tuple):
            other = SaberCrystal(color=other)
        self.red = self.red - other.red
        self.green = self.green - other.green
        self.blue = self.blue - other.blue
        rgb_values = [self.red, self.green, self.blue]
        new_color = [0 if value <=0 else value for value in rgb_values]     
        return SaberCrystal(new_color)

    def __contains__(self, other):
        if isinstance(other, tuple):
            other = SaberCrystal(color=other)
        if other.red <= self.red and other.blue <= self.blue and other.green <= self.green:
            return True
        else:
            return False
