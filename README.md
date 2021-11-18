# Tradutor/Speech

# Sobre o projeto
Nosso projeto visa ajudar pessoas a aprenderem novas palavras de idiomas estrangeiros. Nosso projeto é composto uma RNA treinada por nós, com o objetivo de classficar imagens que o usuario irá enviar para a mesma

## Objetivo do projeto
O projeto tem como objetivo ajudar as pessoas a aprenderem novas palavras em idiomas estrangeiros e também a saber a pronúncia das mesmas

### Como funciona 

 No projeto existem 3 abas, na aba da esquerda é onde fica a parte onde o usuário irá enviar uma imagem, e a RNA irá fazer a classificação da imagem retornando o texto para que o tradutor faça seu papel e traduza para o idioma selecionado. Na aba da direita é onde fica a parte de speech, onde o usuário irá enviar uma imagem, e a IA irá reconhecer o texto que existe na imagem e irá reproduzir o mesmo. Por fim, na aba do meio é onde os dois serviços se juntam, onde o usuário irá enviar uma imagem, a RNA irá fazer a classificação e retornar o texto traduzido, irá enviar o texto para a IA de speech, onde o mesmo irá reproduzir no idioma escolhido.
<hr>  
      
# Tecnologias utilizadas
## Linguagens utilizadas
- :snake: Python

## Bibliotecas/Frameworks utilizadas
- Keras
- Tensorflow
- Pyttsx3
- Dash
- Pytesseract
- Boto3(AWS)

<hr>  

# Como executar o projeto
```bash
git clone https://github.com/GabrielKuroda/AWS-python-translator
# ir para onde o .py do projeto estiver, executar o comando:

python webserver.py

# feito isso o projeto ja estará no ar.Logo após deve se usar o postman ou o insomnia, e utilizar o seguinte JSON para executar o POST:


OBS: GET deve ser realizados no devido endereço: localhost:8000
```
<hr>  

# Como executar o projeto

- [ ] Acréscimo de novas classes
- [ ] Aumento do dataset para o retreinamento da RNA
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
Pedro Henrique Longo https://github.com/PedroHLongo <br>
Wallace Everton Cavalcante de Paiva (https://github.com/WallaceCavalcante) <br>

# Professor 
Vandeir, UNIFAJ - Ciência da Computação 6º semestre
<hr>  
	 
<br>
<br>
