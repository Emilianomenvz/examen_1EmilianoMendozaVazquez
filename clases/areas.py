class Area():
     def __init__(self,x:float,y:float):
          self.__x=x
          self.__y=y
          return
     
     def triangulo (self):
         a= (self.__x*self.__y)/2
         return a
    
     def rectangulo(self):
          a=self.__x * self.__y
          return a
     
     def circulo (self):
          a=3.1416*(self.__x**2)
          return a
          
          