import pandas as pd
import plotly.express as px

data = pd.read_excel("ventas.xlsx")

print(data.head())
print(data.tail())
print(data.shape)

print(data["precio"].head())
print(data["tienda"].head())

print(data[["Ciudad", "País", "precio"]].head())
print(data.describe())

print(data["tienda"].unique())
print(data["tienda"].value_counts())
print(data["Ciudad"].value_counts())
print(data["forma_pago"].value_counts())

print(data.groupby("forma_pago")["precio"].sum().to_frame())

datos_agrupados = data.groupby(["tienda", "forma_pago"])["precio"].sum().to_frame()
datos_agrupados.to_excel("facturacion.xlsx")

px.histogram(data, x="tienda")

grafico = px.histogram(data,
             x = "tienda",
             text_auto=True,
             title="facturacion",
             color="forma_pago")

grafico.show()
grafico.write_html("facturacion.html")

columnas = ['tienda', 'Ciudad', 'País', 'tamaño', 'local_consumo']

for columna in columnas:
    fig = px.histogram(data,
                       x=columna,
                       y='precio',
                       color='forma_pago',
                       text_auto=True,
                       title=f"facturacion por {columna}")
    fig.write_html(f"facturacion_por_{columna}.html")    
    fig.show()

agrupado = data.groupby(['tienda', 'local_consumo']).precio.sum().to_frame()
agrupado.reset_index(inplace=True)
agrupado['acumulado'] = agrupado.groupby('tienda').precio.cumsum()

fig = px.bar(agrupado,
             x='acumulado',
             y="tienda",
             color='tienda',
             text_auto=True,
             range_x=[0,160000],
             animation_frame='local_consumo')
fig.show()