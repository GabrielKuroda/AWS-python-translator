import boto3

#Criando Instancia da API de tradução
client = boto3.client('translate', region_name="us-east-1")
#Texto para traduzir
text = "nombre"
#Chamada do metodo da API do AWS Translator, Text = texto a ser traduzido, SourceLanguageCode = Lingua do texto original, TargetLanguageCode=Lingua a ser traduzida
result = client.translate_text(Text=text, SourceLanguageCode="auto",
    TargetLanguageCode="ja")
#Idiomas
# en - Ingles
# ja - Japones
# pt - Portugues
# es - Espanhol

print(result['TranslatedText'])