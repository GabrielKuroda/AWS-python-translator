import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from app import app
import boto3
import webbrowser
import pandas as pd
from detect import DetectorImg

webbrowser.open("http://127.0.0.1:8050/")

detector = DetectorImg()

input_file = dcc.Upload(
                    id='upload-data',
                    children=html.Div([
                        'Drag and Drop or ',
                        html.A('Select Files')
                    ]),
                    style={
                        'widht':'30%',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin': '10px'
                    },
                    multiple=True
                )

origin_lang = dcc.Dropdown(
        id="originLang",
        options=[
            {'label': 'Portuguese', 'value': 'pt'},
            {'label': 'Japanese', 'value': 'ja'},
            {'label': 'Spanish', 'value': 'es'},
            {'label': 'English', 'value': 'en'}
        ],
        multi=False,
        value="en"
    )

target_lang = dcc.Dropdown(
        id="targetLang",
        options=[
            {'label': 'Portuguese', 'value': 'pt'},
            {'label': 'Japanese', 'value': 'ja'},
            {'label': 'Spanish', 'value': 'es'},
            {'label': 'English', 'value': 'en'}
        ],
        multi=False
    )

app.layout = dbc.Container([
    dcc.Loading(
        id="loading-1",
        type="default",
        children=html.Div
        ([
            html.Div(
                html.Img(src='/assets/logo.jpeg', style={'height':'130px', 'width':'220px', "display": "block", 'margin-left': 'auto', 'margin-right': 'auto'})),
            html.Hr(),
            html.Div(id='title_text',
                    children=html.H1('Translator with IA',style={"textAlign": "center"})),
            html.Hr(),
            html.Div(id='origin_text',
                    children=html.H3('Origin Language')),
            dbc.Col(origin_lang, width=12),
            html.Hr(),
            html.Div(id='target_text',
                    children=html.H3('Target Language')),
            dbc.Col(target_lang, width=12),
            html.Hr(),
            html.Div(id='image_text',
                    children=html.H3('Image')),
            dbc.Col(input_file, width=12),
            html.Div(
                [
                html.Br(),
                html.Div(id='output-image-upload'),
                html.Hr()
            ]),
            html.Div(id='facul_text',
                    children=html.Pre('University Center of Jaguariúna (UniFAJ)', style={'textAlign': 'center', 'margin': '10px'})),
            html.Div(id='student_text',
                    children=html.Pre('Students:  Gabriel Kuroda, Leonardo Santos', style={'textAlign': 'center', 'margin': '10px'})),
            html.Div(id='professor_text',
                    children=html.Pre('Students:  Gabriel Kuroda, Leonardo Santos', style={'textAlign': 'center', 'margin': '10px'})),
        ])
    )
])


@app.callback(Output('title_text', 'children'),
              Output('origin_text', 'children'),
              Output('target_text', 'children'),
              Output('image_text', 'children'),
              Output('facul_text', 'children'),
              Output('student_text', 'children'),
              Output('professor_text', 'children'),
              [Input('originLang', 'value')])
def update_page(value):
    labelOrigin = "Origin Language"
    labelTarget = "Target Language"
    labelTitle = "Translator with IA"
    labelImage = "Image"
    labelFacul = 'University Center of Jaguariúna (UniFAJ)'
    labelStudents = 'Students:  Gabriel Kuroda, Leonardo Santos'
    labelProfessor = 'Professor:  Vandeir Aniceto'
    
    title = translate(labelTitle,value,'en')
    textOrigin = translate(labelOrigin,value,'en')
    textTarget = translate(labelTarget,value,'en')
    image = translate(labelImage,value,'en')
    facul = translate(labelFacul,value,'en')
    students = translate(labelStudents,value,'en')
    professor = translate(labelProfessor,value,'en')
    
    return html.H1(title,style={"textAlign": "center"}), html.H3(textOrigin), html.H3(textTarget), html.H3(image) , html.Pre(facul, style={'textAlign': 'center', 'margin': '10px'}) , html.Pre(students, style={'textAlign': 'center', 'margin': '10px'}) , html.Pre(professor, style={'textAlign': 'center', 'margin': '10px'})

def parse_contents(contents,origin,target):
    score = detector.getScore(contents)
    result = detector.getResult()
    return dbc.Row([
                    dbc.Col([
                        html.H3(translate('Analyzed Image: ',origin,'en')),
                        html.Br(),
                        html.H5(translate(result,origin,'en')), 
                        html.Br(),
                        html.Div(html.Img(src=contents, style={'height':'50%', 'width':'80%'})),
                    ],),
                    dbc.Col([
                        html.H3(translate('Result: ',origin,'en')), 
                        html.Br(),
                        html.H5(score), 
                        html.Br(),
                        html.H5(translate(result,target,origin)), 
                    ],)
            ])


@app.callback([Output('output-image-upload', 'children')],
              [Input('upload-data', 'contents'), Input("originLang", "value"), Input("targetLang", "value")],
              [State('upload-data', 'filename'),
              State('upload-data', 'last_modified')])

def update_output(list_of_contents, origin,target, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [parse_contents(c,origin,target) for c, n, d in zip(list_of_contents, list_of_names, list_of_dates)]
        return children


def translate(phrase,target,origin):
    credencials = pd.read_csv('credencials\Credencials.csv', sep=',', encoding='utf-8')
        
    client = boto3.client('translate', region_name="us-east-1",aws_access_key_id= credencials['Access key ID'][0],
        aws_secret_access_key= credencials['Secret access key'][0])

    return client.translate_text(Text=phrase, SourceLanguageCode=origin,TargetLanguageCode=target)['TranslatedText']
        
if __name__=='__main__':
    app.run_server(debug=False)