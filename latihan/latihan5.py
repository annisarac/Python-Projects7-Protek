nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	{'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
        {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
        {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
        {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('============================================================')
print('NIM'.ljust(15), 'NAMA'.ljust(15), 'N.MID'.ljust(15), 'N.UAS'.ljust(15),)
print('------------------------------------------------------------')

for i in nilai:
    print(i['nim'].ljust(15), i['nama'].ljust(15), str(i['mid']).ljust(15), str(i['uas']).ljust(15)) 

print('------------------------------------------------------------')
