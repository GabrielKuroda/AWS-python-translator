# Sobre o projeto
Nosso projeto visa ajudar pessoas a aprenderem novas palavras de idiomas estrangeiros. Nosso projeto é composto uma RNA treinada por nós, com o objetivo de               classficar imagens que o usuario irá enviar para a mesma
### Como funciona      
 O usuário irá enviar uma imagem, onde está imagem será classificada por uma rede neural, após isso deverá ser escolhido o idioma preferido para a tradução da imagem que foi classificada anteriormente
<hr>  
      
# Tecnologias utilizadas 
#### :snake: Python
<hr>  

# Como executar o projeto
```bash
git clone https://github.com/GabrielKuroda/AWS-python-translator
# ir para onde o .py do projeto estiver, executar o comando:

python webserver.py

# feito isso o projeto ja estará no ar.Logo após deve se usar o postman ou o insomnia, e utilizar o seguinte JSON para executar o POST:

{
    "image":"url da imagem desejada",
    "languageTarget":" idioma alvo",
    "languageOrigin":"idioma de origem",
    "accessKey":"segredo",
    "secretAccessKey":"segredo"
}

OBS: GET e POST devem ser realizados no devido endereço: localhost:8000
```
<hr>  

# Próximos objetivos

- [ ] Acréscimo de novas classes
- [ ] Aumento do dataset para o retreinamento da RNA
<hr>  

# Autores
Décio Manarini Neto <br>
Gabriel Tatsuya Avi Kuroda (https://github.com/GabrielKuroda) <br>
Leonardo Aparecido dos Santos (https://github.com/leonardosantos1) <br>
Pedro Henrique Longo https://github.com/PedroHLongo <br>
Wallace Everton Cavalcante de Paiva - 11921375
<hr>  
	 
<br>
<br>
