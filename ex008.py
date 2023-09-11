medida =float(input('Uma distância em metros:'))
cm = medida * 100
mm = medida * 1000
dcm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('A medida de {} m, corresponde a:{} cm,\n {} mm,\ndcm {},\ndam {},\nhm {},\nkm {} '.format(medida, cm, mm, dcm, dam, hm, km))

