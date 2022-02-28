jalan="Y"
while jalan=="Y":
  tahun=int(input("Tahun :"))
  if tahun>1500:
    if tahun % 400==0:
        ket="Tahun Kabisat"
    elif (tahun % 4==0) and (tahun % 100>0):
        ket="Tahun Kabisat"
    else:
        ket="Bukan Tahun Kabisat"    
  else:
    if tahun % 4==0:
        ket="Tahun Kabisat"
    else:
        ket="Bukan Tahun Kabisat"

  print(ket)
  jalan=input("Masukkan tahun lagi [Y/T] ?:")
  print("")
