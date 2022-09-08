def Ppunto(Vector1, Vector2, size):
  producto = 0
  for i in range(0,size):
    producto = producto + (Vector1[i] * Vector2[i])
  return producto

a = [1,2,3]
b = [4,5,6] 
print (Ppunto(a,b, 3))