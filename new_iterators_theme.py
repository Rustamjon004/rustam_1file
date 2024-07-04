
 #   print(i)
 # 
class Finobacci :
     def __init__(self,son_n):
         self.son_n = son_n
         self.n = 0
         self.a,self.b = 0,1
         
     def __iter__(self):
         return self
     
     def __next__(self):
         if self.n >= self.son_n:
           raise StopIteration
         if self.n == 0: 
           self.n +=1
           return 0
         elif self.n == 1:
             self.n +=1
             return 1
         else:
             self.x,self.y = self.b,self.a + self.b
             self.a += 1
             return self.a
         
fib_iter = Finobacci(3)
for fib in fib_iter:
    print(fib)

     
              
     
     
      