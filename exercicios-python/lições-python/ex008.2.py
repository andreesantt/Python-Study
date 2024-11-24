medida = float(input('Digite uma distância: '))
km = medida / 1000
hm = km / 100
dam = hm / 1000
dm = dam * 10
cm = dm * 100
mm = cm * 1000
print('O valor de {}m convertido vale: {}km, {}hm, {}dam\n {}dm, {}cm, {}mm'.format(medida, km, hm, dam, dm, cm, mm))