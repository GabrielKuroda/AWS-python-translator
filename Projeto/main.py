import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from app import app
import boto3
import webbrowser
import pandas as pd
from translator.detect import DetectorImg
from speech.analitc import Analytics

webbrowser.open("http://127.0.0.1:8050/")

detector = DetectorImg()
analy = Analytics()

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

input_fileSpeech = dcc.Upload(
                    id='upload-data-speech',
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

input_file_integration  = dcc.Upload(
                    id='upload-data-integration',
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

origin_lang_integration = dcc.Dropdown(
        id="origin-lang-integration",
        options=[
            {'label': 'Portuguese', 'value': 'pt'},
            {'label': 'Japanese', 'value': 'ja'},
            {'label': 'Spanish', 'value': 'es'},
            {'label': 'English', 'value': 'en'}
        ],
        multi=False,
        value="en"
    )

target_lang_integration  = dcc.Dropdown(
        id="target-lang-integration",
        options=[
            {'label': 'Portuguese', 'value': 'pt'},
            {'label': 'Japanese', 'value': 'ja'},
            {'label': 'Spanish', 'value': 'es'},
            {'label': 'English', 'value': 'en'}
        ],
        multi=False
    )

choose_lang = dcc.RadioItems(id='lang_chosen',
    options=[{'label':' Português   .', "value": 'por'}, {'label':' Inglês ', "value": 'eng'}
    ,{'label':' Japonês ', "value": 'jap'}, {'label':' Espanhol ', "value": 'esp'}],
    value='jap',
    labelStyle={}
) 

translator = dcc.Loading(
                    id="loading-1",
                    type="default",
                    children=html.Div
                    ([
                        html.Div(
                            html.Img(src='/assets/logo.jpeg', style={'height':'130px', 'width':'220px', "display": "block", 'margin-left': 'auto', 'margin-right': 'auto'})),
                        html.Hr(),
                        html.Div(id='title_text',
                                children=html.H1('Translator with AI',style={"textAlign": "center"})),
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
                                children=html.Pre('Professor:  Vandeir Aniceto', style={'textAlign': 'center', 'margin': '10px'})),
                    ])
                )


speakerTranslator = dcc.Loading(
                        id="loading_integration",
                        type="default",
                        children=html.Div
                        ([
                            html.Div(
                                html.Img(src='/assets/logo.jpeg', style={'height':'130px', 'width':'220px', "display": "block", 'margin-left': 'auto', 'margin-right': 'auto'})),
                            html.Hr(),
                            html.Div(id='title_text_integration',
                                    children=html.H1('Translator/Speech',style={"textAlign": "center"})),
                            html.Hr(),
                            html.Div(id='origin_text_integration',
                                    children=html.H3('Origin Language')),
                            dbc.Col(origin_lang_integration, width=12),
                            html.Hr(),
                            html.Div(id='target_text_integration',
                                    children=html.H3('Target Language')),
                            dbc.Col(target_lang_integration , width=12),
                            html.Hr(),
                            html.Div(id='image_text_integration',
                                    children=html.H3('Image')),
                            dbc.Col(input_file_integration , width=12),
                            html.Div(
                                [
                                html.Br(),
                                html.Div(id='output-image-upload-integration'),
                                html.Hr()
                            ]),
                            html.Div(id='facul_text_integration',
                                    children=html.Pre('University Center of Jaguariúna (UniFAJ)', style={'textAlign': 'center', 'margin': '10px'})),
                            html.Div(id='student_text_integration',
                                    children=html.Pre('Students:  Gabriel Kuroda, Leonardo Santos, Pedro Longo, Decio, Wallace', style={'textAlign': 'center', 'margin': '10px'})),
                            html.Div(id='professor_text_integration',
                                    children=html.Pre('Professor:  Vandeir Aniceto', style={'textAlign': 'center', 'margin': '10px'})),
                        ])
                    )

speech = dbc.Container([
    html.Div(html.Img(src='/assets/logo.jpeg', style={'height':'130px', 'width':'220px', "display": "block", 'margin-left': 'auto', 'margin-right': 'auto'})),
    html.Hr(),
    dbc.Row(dbc.Col(html.H1("Projeto para Inteligência Artificial 2",style={"textAlign": "center"}), width=12)),
    html.Hr(),

    dbc.Col([input_fileSpeech, choose_lang], width=12),

    html.Div(
        [
        html.Br(),
        html.Div(id='output-image-upload-speech'),
        html.Hr(),
        html.Pre('Centro Universitário de Jaguariúna (UniFAJ)', style={'textAlign': 'center', 'margin': '10px'}),
        html.Pre('Alunos: Pedro Longo, Decio, Wallace', style={'textAlign': 'center', 'margin': '10px'}),
    ],
    )
])

app.layout = dbc.Container([
    html.Div([
        dcc.Tabs([
            dcc.Tab(id="tab-translator",label='Translator with AI', children=[
                translator
            ]),
            dcc.Tab(id="tab-integration",label='Translator/Speech', children=[
                speakerTranslator
            ]),
            dcc.Tab(id="tab2",label='Speech with AI', children=[
                speech
            ]),
        ])
    ])
])


@app.callback(Output('title_text', 'children'),
              Output('origin_text', 'children'),
              Output('target_text', 'children'),
              Output('image_text', 'children'),
              Output('facul_text', 'children'),
              Output('student_text', 'children'),
              Output('professor_text', 'children'),
              Output('tab-translator','label'),
              [Input('originLang', 'value')])
def update_page(value):
    labelOrigin = "Origin Language"
    labelTarget = "Target Language"
    labelTitle = "Translator with AI"
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
    
    return html.H1(title,style={"textAlign": "center"}), html.H3(textOrigin), html.H3(textTarget), html.H3(image) , html.Pre(facul, style={'textAlign': 'center', 'margin': '10px'}) , html.Pre(students, style={'textAlign': 'center', 'margin': '10px'}) , html.Pre(professor, style={'textAlign': 'center', 'margin': '10px'}),title

@app.callback(Output('title_text_integration', 'children'),
              Output('origin_text_integration', 'children'),
              Output('target_text_integration', 'children'),
              Output('image_text_integration', 'children'),
              Output('facul_text_integration', 'children'),
              Output('student_text_integration', 'children'),
              Output('professor_text_integration', 'children'),
              Output('tab-integration','label'),
              [Input('origin-lang-integration', 'value')])
def update_page(value):
    labelOrigin = "Origin Language"
    labelTarget = "Target Language"
    labelTitle = "Translator/Speech"
    labelImage = "Image"
    labelFacul = 'University Center of Jaguariúna (UniFAJ)'
    labelStudents = 'Students:  Gabriel Kuroda, Leonardo Santos, Pedro Longo, Decio, Wallace'
    labelProfessor = 'Professor:  Vandeir Aniceto'
    
    title = translate(labelTitle,value,'en')
    textOrigin = translate(labelOrigin,value,'en')
    textTarget = translate(labelTarget,value,'en')
    image = translate(labelImage,value,'en')
    facul = translate(labelFacul,value,'en')
    students = translate(labelStudents,value,'en')
    professor = translate(labelProfessor,value,'en')
    
    return html.H1(title,style={"textAlign": "center"}), html.H3(textOrigin), html.H3(textTarget), html.H3(image) , html.Pre(facul, style={'textAlign': 'center', 'margin': '10px'}) , html.Pre(students, style={'textAlign': 'center', 'margin': '10px'}) , html.Pre(professor, style={'textAlign': 'center', 'margin': '10px'}),title


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

def parse_contents_integration(contents,origin,target):
    score = detector.getScore(contents)
    result = detector.getResult()
    traducao = translate(result,target,origin)
    path_audio = analy.say(traducao)
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
                        html.H5(traducao),
                        html.Br(),
                        html.Audio(src=path_audio, controls=True)
                    ],)
            ])

@app.callback([Output('output-image-upload-integration', 'children')],
              [Input('upload-data-integration', 'contents'), Input("origin-lang-integration", "value"), Input("target-lang-integration", "value")],
              [State('upload-data-integration', 'filename'),
              State('upload-data-integration', 'last_modified')])

def update_output_int(list_of_contents, origin,target, list_of_names, list_of_dates):
    if target == 'ja':
        analy.LANG = 'jap'
    elif target == 'en':
        analy.LANG = 'eng'
    elif target == 'es':
        analy.LANG = 'esp'
    elif target == 'pt':
        analy.LANG = 'por'
    if list_of_contents is not None:
        children = [parse_contents_integration(c,origin,target) for c, n, d in zip(list_of_contents, list_of_names, list_of_dates)]
        return children

def parse_contents_speech(contents):
    texto = analy.read(contents)
    path_audio = analy.say(texto)
    return dbc.Row([
                    dbc.Col([
                        html.H5('Imagem Analisada:'),
                        html.Br(),
                        html.Div(html.Img(src=contents, style={'height':'50%', 'width':'80%'})),
                    ],),
                    dbc.Col([
                        html.H5('Texto extraido da imagem:'), 
                        html.Audio(src=path_audio, controls=True),
                        html.Br(),
                        html.P(texto),
                    ],)
            ])

@app.callback([Output('output-image-upload-speech', 'children')],
              [Input('upload-data-speech', 'contents'), Input("lang_chosen", "value")],
              [State('upload-data-speech', 'filename'),
              State('upload-data-speech', 'last_modified')])

def update_output(list_of_contents, lang, list_of_names, list_of_dates):
    if list_of_contents is not None:
        analy.LANG = lang
        children = [parse_contents_speech(c) for c, n, d in zip(list_of_contents, list_of_names, list_of_dates)]
        return children

def translate(phrase,target,origin):
    credencials = pd.read_csv('credencials\Credencials.csv', sep=',', encoding='utf-8')
        
    client = boto3.client('translate', region_name="us-east-1",aws_access_key_id= credencials['Access key ID'][0],
        aws_secret_access_key= credencials['Secret access key'][0])

    return client.translate_text(Text=phrase, SourceLanguageCode=origin,TargetLanguageCode=target)['TranslatedText']
        
if __name__=='__main__':
    app.run_server(debug=False)
