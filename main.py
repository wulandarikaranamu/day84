#nilai acak
import random 

randomInteger = random.randint(1,8)
print(randomInteger)

randomFloat = random.random()*3
print(randomFloat)

merry = random.randint(1,20)
print(f"nilai untuk merry adalah {merry}")


merry = random.random()*4
print(f"nilai untuk merry adalah {merry}")


random_kanan = random.randint(0,1)
if random_kanan == 1:
    print("benar")
else:
    print("salah")