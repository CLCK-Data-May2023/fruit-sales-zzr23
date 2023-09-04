data = {
    'Fruit': ['Apples', 'Bananas'],
    'Sales': [35, 21]
}
df = pd.DataFrame(data)

df.to_csv('fruit.csv', index=False)# add your code here

