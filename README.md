# Tradutor/Speech

# Sobre o projeto
Nosso projeto visa ajudar pessoas a aprenderem novas palavras de idiomas estrangeiros junto com a pronúncia da mesma. Ele é composto por uma RNA treinada por nós, com o objetivo de classficar imagens que o usuário irá enviar para a mesma.

## Objetivo do projeto
O projeto tem como objetivo ajudar as pessoas a aprenderem novas palavras em idiomas estrangeiros e também a saber a pronúncia das mesmas.

### Como funciona 

 No projeto existem 3 abas, na primeira aba é onde fica a parte onde o usuário irá enviar uma imagem e a RNA irá fazer a classificação da imagem retornando o texto para que o tradutor faça seu papel e traduza para o idioma selecionado. Na terceira aba é onde fica a parte de speech, onde o usuário irá enviar uma imagem e a IA irá reconhecer o texto que existe na imagem e irá reproduzir o mesmo. Por fim, na segunda aba é onde os dois serviços se juntam, onde o usuário irá enviar uma imagem, a RNA irá fazer a classificação e retornar o texto traduzido, irá enviar o texto para a IA de speech, onde o mesmo irá reproduzir no idioma escolhido.
<hr>  
      
# Tecnologias utilizadas
## Linguagens utilizadas
- :snake: Python

## Bibliotecas/Frameworks/API utilizadas
- Keras
- Tensorflow
- Dash
- Pyttsx3
- Pytesseract
- Boto3(AWS)
- PIL
- Pandas

<hr>  

# Como executar o projeto
```bash
git clone https://github.com/GabrielKuroda/AWS-python-translator

É necessario instalar algumas dependências de bibliotecas que foram utilizadas, segue os comandos abaixo:

pip install keras
pip install tensorflow
pip install dash
pip install pyttsx3
pip install pytesseract
pip install boto3
pip install Pillow
pip install pandas

Além de realizar o pip do pytesseract, é necessário instalá-lo de acordo com seu windows(32/64):

https://github.com/UB-Mannheim/tesseract/wiki

Ele deverá ser instalado no caminho C:\Program Files\Tesseract-OCR\tesseract.exe, ou caso queira adicioná-lo em outro caminho, deverá alterar a variável de ambiente PATH_TE que se encontra no AWS-python-translator\Projeto\speech\config.txt para o caminho de instalação selecionado.


Também deverá ser instalado no seu windows os idiomas utilizados no projeto, que no caso são:

- Inglês(United States)
- Espanhol(Espanã)
- Português(Brasil)
- Japonês

O caminho a seguir será pesquisar no seu windows "Configurações de Idioma"
Após clicar nas configuração deverá clicar em "Adicionar um idioma" e nisso instalar os idiomas citados acima.


Para ser possível rodar o tradutor é necessário criar uma pasta no AWS-python-translator\Projeto\ com o nome credencials, dentro dessa pasta deverá ser colocado suas credencias da AWS como um arquivo csv, que deverá ser renomeado para Credencials.csv

Para obter esse arquivo é necessário possuir uma conta na AWS e ele é obtido através do serviço IAM na aba usuários.


Após realizado todas as etapas anteriores, é necessário ir para \AWS-python-translator\Projeto e executar o comando:

python main.py

Feito isso o projeto ja estará no ar.
```
<hr>  

# Observações do projeto

- Nossa RNA não irá funcionar corretamente com formatores de imagens diferentes de: .jpg, .jpeg

- Classes utilizadas no projeto: ['abelha', 'aranha', 'bicicleta', 'borboleta', 'cachorro', 'carro', 'cavalo', 'coelho', 'dente-de-leao', 'elefante', 'esquilo', 'gafanhoto', 'galinha', 'gato', 'girafa', 'girassol', 'hamster', 'joaninha', 'leao', 'libelula', 'margarida', 'monitor', 'mosquito', 'moto', 'mouse', 'ovelha', 'panda', 'rosa', 'tartaruga', 'teclado', 'tulipa', 'vaca', 'veado', 'zebra']

- Nosso dataset foi removido do github por motivos que os commits estavam passando do tamanho suportado pelo github (iremos adicionar um link, onde terá a opção de realizar download do dataset utilizado para o treino da RNA)

<hr>  

# Autores
Décio Manarini Neto (https://github.com/DecioManarini) <br>
Gabriel Tatsuya Avi Kuroda (https://github.com/GabrielKuroda) <br>
Leonardo Aparecido dos Santos (https://github.com/leonardosantos1) <br>
Pedro Henrique Longo (https://github.com/PedroHLongo) <br>
Wallace Everton Cavalcante de Paiva (https://github.com/WallaceCavalcante) <br>
<hr>

# Referências utilizadas
## Documentações utilizadas
- https://keras.io/api/
- https://www.tensorflow.org/api_docs
- https://pyttsx3.readthedocs.io/en/latest/
- https://dash.plotly.com/
- https://pypi.org/project/pytesseract/
- https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
- https://pillow.readthedocs.io/en/stable/
- https://pandas.pydata.org
<hr>

# Professor 
Vandeir, UNIFAJ - Ciência da Computação 6º semestre
<hr>  
<br>
<br>
