nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	{'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
        {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
        {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
        {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('==========================================================================================')
print('NIM'.ljust(15), 'NAMA'.ljust(15), 'N.MID'.ljust(15), 'N.UAS'.ljust(15), 'N.AKHIR'.ljust(15), 'STATUS'.ljust(15))
print('------------------------------------------------------------------------------------------')

nilaiAkhir = []
for x in nilai:
    rumus = (x['mid'] + (2*x['uas']))/3
    bulat = int(rumus)
    nilaiAkhir.append(bulat)
    if (bulat >= 60):
        status = 'LULUS'
    else:
        status = 'TIDAK LULUS'

for i in range(len(nilai)):
    print(nilai[i]['nim'].ljust(15), nilai[i]['nama'].ljust(15), str(nilai[i]['mid']).ljust(15),
          str(nilai[i]['uas']).ljust(15), str(nilaiAkhir[i]).ljust(15), str(status))

print('------------------------------------------------------------------------------------------')
