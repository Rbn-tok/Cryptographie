def crypto(mot,dec,base):
  n=len(mot)
  deca=dec
  motcrypte=""
  
  
  for i in range(0,n):
    if mot[i] in base :
      
      indexmot=base.index(mot[i])
      pas=len(base)-(indexmot+1)
     
    
      if pas <deca :
        indexmot=deca -pas
        motcrypte +=base[indexmot-1]
      else :
        motcrypte +=base[indexmot + deca]
    
  return motcrypte

base="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ&0123456789"
mot="papa"  
print(mot)
print(crypto(mot,5,base))
