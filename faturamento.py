faturamento = {
    'SP' : 67836.43,
    'RJ' : 36678.66,
    'MG' : 29229.88,
    'ES' : 27165.48,
    'Outros' : 19849.53
}

total = faturamento.get('SP') + faturamento.get('RJ') + faturamento.get('MG') + faturamento.get('ES') + faturamento.get('Outros')

for c, f in faturamento.items():
    print(f'{c} tem um faturamento equivalente a {f/total * 100:.2f}% do total')