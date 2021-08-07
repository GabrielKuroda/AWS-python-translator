import boto3
import click

@click.command()
@click.option('--phrase', prompt='Put in a phrase in any language to translate',
    help='this is a tool that traslate text')
def action(phrase):
    #Criando Instancia da API de tradução
    client = boto3.client('translate', region_name="us-east-1")
    
    #Print?
    click.echo(click.style(f"Translate phrase: {phrase}", fg='red'))

    #Chamada do metodo da API do AWS Translator, Text = texto a ser traduzido, SourceLanguageCode = Lingua do texto original, TargetLanguageCode=Lingua a ser traduzida
    result = client.translate_text(Text=phrase, SourceLanguageCode="auto",
        TargetLanguageCode="ja")
        
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

