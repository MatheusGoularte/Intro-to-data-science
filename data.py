import pandas as pd 


uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv"
filmes = pd. read_csv (uri)

filmes.head()


filmes.columns = ["filme id", "titulo", "generos"]
print(filmes)

uri= "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv"
notas = pd. read_csv (uri)
notas.columns = ["usuario id", "filme id", "nota", "momento"]
print(notas)


notas["nota"].head()
notas["nota"].unique() # series

notas["nota"].mean() 
notas["nota"].min()
notas["nota"].max()


notas.describe()
print(notas.describe())