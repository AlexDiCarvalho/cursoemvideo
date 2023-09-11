larg =float(input('Qual largura da sua parede?:'))
alt =float(input(' Qual altura da sua parede?:'))
area = larg * alt
print('A area total da parede em m²:{:.2f}'.format(larg * alt))
tinta = area / 2
print('A sua parede de dimensão {}, precisará de {} L de tinta'.format(area, tinta))
