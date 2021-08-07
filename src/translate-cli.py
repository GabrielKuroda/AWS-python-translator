import boto3
import click

def action():
    #Criando Instancia da API de tradução
    client = boto3.client('translate', region_name="us-east-1")
    language = input('Para qual idioma irá traduzir?\n en - Ingles\n ja - Japones\n pt - Portugues\n es - Espanhol\n ')
    phrase = input('Valor a ser traduzido: ')
    #Print?
    click.echo(click.style(f"Translate phrase: {phrase}", fg='red'))

    #Chamada do metodo da API do AWS Translator, Text = texto a ser traduzido, SourceLanguageCode = Lingua do texto original, TargetLanguageCode=Lingua a ser traduzida
    result = client.translate_text(Text=phrase, SourceLanguageCode="auto",
        TargetLanguageCode=language)
        
    text = result['TranslatedText']
    
    #Print?
    click.echo(click.style(f"{text}", bg='blue', fg='white'))    
    #Idiomas
    # en - Ingles
    # ja - Japones
    # pt - Portugues
    # es - Espanhol
    
#Obrigatório para rodar linhas de comando
if __name__=='__main__':
    action()