mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('==============================================================================')
print('NAMA'.ljust(15), 'NAMA MAHASISWA'.ljust(20), 'TGL LAHIR'.ljust(15), 'TEMPAT LAHIR'.ljust(15))
print('------------------------------------------------------------------------------')

data = mhs[0]
pisah = data.split(':')
data2 = pisah[2]
tanggal = data2.split('-')
urut = tanggal[2], tanggal[1], tanggal[0]
gabung = '/'.join(urut)
del pisah[2]

print((pisah[0]).ljust(15), (pisah[1]).ljust(20), (gabung).ljust(15), (pisah[2]))

data1 = mhs[1]
pisah1 = data1.split(':')
data3 = pisah1[2]
tanggal1 = data3.split('-')
urut1 = tanggal1[2], tanggal1[1], tanggal1[0]
gabung1 = '/'.join(urut1)
del pisah1[2]

print((pisah1[0]).ljust(15), (pisah1[1]).ljust(20), (gabung1).ljust(15), (pisah1[2]))

data2 = mhs[2]
pisah2 = data2.split(':')
data4 = pisah2[2]
tanggal2 = data4.split('-')
urut2 = tanggal2[2], tanggal2[1], tanggal2[0]
gabung2 = '/'.join(urut2)
del pisah2[2]

print((pisah2[0]).ljust(15), (pisah2[1]).ljust(20), (gabung2).ljust(15), (pisah2[2]))

print('------------------------------------------------------------------------------')

