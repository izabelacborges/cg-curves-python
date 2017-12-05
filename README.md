# Curvas Paramétricas

> Trabalho proposto na disciplina de Computação Gráfica. Propõe a implementação
> dos algoritmos de curva de Bézier e Interpolação.

## Ferramentas utilizadas

* Python 3.6
* Numpy (1.13.3)
* Matplotlib (2.1.0)
* Jupyter notebooks

## Implementação

O trabalho foi implementado em Python 3.6 utilizando as bibliotecas `numpy` pela
facilidade em tratar de operações numéricas, e `matplotlib` para plotar as
imagens das curvas. A interatividade é feita pelo uso do módulo `nbagg` dentro
dos Jupyter notebooks.

## Instalação

### Linux

#### Python

Abra o terminal e tente `python3 --version`. Caso este comando não te retorne um
número de versão, execute os comandos abaixo:

```shell
$ sudo apt-get update
$ sudo apt-get install python3.6
```

#### Libs

Para instalar os módulos utilizados execute o comando abaixo no terminal:

```shell
$ sudo pip3 install -U numpy matplotlib jupyter
```

### Windows

#### Python

Acesse o site do [Python](https://www.python.org/downloads/windows/) e instale o
Python 3 mais recente (3.6.3 no momento da escrita deste documento).

Nas suas variáveis de ambiente, adicione o seguinte trecho ao seu **PATH**:

```
C:\Python36\;C:\Python36\Scripts\
```

#### Libs

Para instalar os módulos utilizados execute o comando abaixo no prompt de
comando:

```shell
$ pip3 install -U numpy matplotlib jupyter
```

### Mac OS X

#### Python

Abra o terminal e tente `python3 --version`. Caso este comando não te retorne um
número de versão, execute os comandos abaixo:

```shell
$ brew install python3
```

#### Libs

Para instalar os módulos utilizados execute o comando abaixo no terminal:

```shell
$ pip3 install -U numpy matplotlib jupyter
```

### Clonando o projeto

Usando o Git você irá clonar este projeto. Abra seu terminal/prompt de comando,
navegue até o diretório de escolha e execute:

```git
git clone https://github.com/izabelacborges/cg-curves-python.git
```

### Configurando e Executando Jupyter Notebooks

#### Configurando

Dentro do diretório `cg-curves-python` você irá abrir o terminal/prompt de
comando e executar:

```shell
jupyter notebook
```

O serviço ira gerar uma url na forma: `http://localhost:<porta>/?token=<token>`
que você deverá copiar e colar no seu navegador.

Você então estará numa interface/IDE interativa do Python chamada Jupyter.

#### Executando

Na interface/IDE Jupyter você terá uma visão de todos os arquivos e diretórios a
partir de onde lançou o comando no terminal (seguindo este tutorial você deverá
estar dentro do `cg-curves-python`). Deverá existir um arquivo chamado
`curves.ipynb`, clique nele por favor.

Agora você já está no ambiente interativo! Para executar o código, você deverá
clicar na primeira célula e apertar `Shift + Enter` sucessivamente até que seja
gerado um grid interativo com o título 'Figure 1'.

Para plotar as curvas você deve marcar os pontos desejados clicando com o botão
esquerdo do mouse, e enfim clicar no grid com o botão direito do mouse. (Se tudo
der certo,) A curva será gerada a partir destes cliques, mostrando além da curva
as retas entre os pontos.

Os resultados gerados foram as imagens a seguir:

#### Bezier

![](https://github.com/izabelacborges/cg-curves-python/blob/master/imagens/bezier.png)

#### Interpolada

![](https://github.com/izabelacborges/cg-curves-python/blob/master/imagens/interpolada.png)
