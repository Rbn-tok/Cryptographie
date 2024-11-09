def crypter(mot,dec,base_cle):
  n=len(mot)
  deca=dec
  motcrypte=""
  base=base_cle
  for i in range(0,n):
    if mot[i] in base :
      indexmot=base.index(mot[i])
      distance=len(base)-(indexmot+1)
      if distance <deca :
        indexmot=deca -distance
        motcrypte +=base[indexmot-1]
      else :
        motcrypte +=base[indexmot + deca]
    
  return motcrypte


def decrypter(mot,dec,base_cle):
  n=len(mot)
  deca=dec
  motcrypte=""
  base=base_cle
  for i in range(0,n):
    if mot[i] in base :
      indexmot=base.index(mot[i])
      distance=len(base)-(indexmot+1)
      
      if indexmot <deca :
        indexmot=len(base)-(deca-indexmot)
        motcrypte +=base[indexmot]
      else :
        motcrypte +=base[indexmot-deca]
  return motcrypte

base1="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ&012345678"
base2="abcdefghijklmnopqrstuvwxyz"
decalage=10
mot="papa"  
mot_crypter=crypter(mot,decalage, base1)
mot2="abcd"

print(mot)
print(crypter(mot,5,base1))
print(crypter(mot,5,base2))
print("mot crypter ",mot ," : ",mot_crypter)
print("décrypter ",mot_crypter," : ",decrypter(mot_crypter,decalage,base1))
