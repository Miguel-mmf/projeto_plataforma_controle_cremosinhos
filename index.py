import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from app import server
from apps import page_1
from apps import page_2
from apps import apoio_layout

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                              Rotinas de Apoio
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def gera_layout():

    return html.Div(
        [
            # header
            html.Div(
                [
                    html.H1(
                        'Plataforma Cremosinho',
                        className='title_style'
                    ),

                    html.H6(
                        'Sousa - PB 2021',
                        className='title_style'
                    ),
                ],
                className='wind__speed__container',
                style={'height':'120px'}
            ),

            html.Div(
                [
                    html.P(
                        'Versão 0.1 - fevereiro 2021',
                        className='title_style',
                        style={'margin-top':'10px'}
                    ),
        
                    html.Div(
                        [
                            html.Label(
                                'Para acessar a página 1, selecione o botão abaixo:',
                                className='descricao_index_style'
                            ),

                            dcc.Link('page 1',
                                href='/apps_v01/page_1',
                                className='button button_link_style',
                            )
                        ],
                        className='one-half column',
                    ),

                    html.Div(
                        [
                            html.Label(
                                'Para acessar a página 2, selecione o botão abaixo:',
                                className='descricao_index_style'
                            ),

                            dcc.Link('page 2',
                                href='/apps_v01/page_2',
                                className='button button_link_style',
                            )
                        ],
                        className='one-half column',
                    ),
                ],
                className='wind__speed__container',
                style={'height':'275px'}
            ),
        
            # logos (CEAR e UFPB)
            html.Div(
                [
                    html.Div(
                        [
                            html.Img(
                                # src= app.get_asset_url('image/'),
                                title='',
                                alt='',
                                className='cear_ufpb',
                            )
                        ],
                        className='six columns box_cear_ufpb',
                    ),

                    html.Div(
                        [
                            html.Img(
                                # src= app.get_asset_url('image/'),
                                title='',
                                alt='',
                                className='cear_ufpb',
                            )
                        ],
                        className='six columns box_cear_ufpb',
                    ),
                ],
                style={'height':'225px'}
            ),

            # Rodapé
            apoio_layout.gera_rodape(),
        ]
    )

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                       Fim das Rotinas de Apoio
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++ LAYOUT  ++++++++++++++++

app.layout = html.Div(
    [
        dcc.Location(
            id='url',
            refresh=False
        ),

        html.Div(
            children = gera_layout(),
            id='page-content',
        ),
    ]
)

# ++++++++++++++++ CALLBACKS  ++++++++++++++++

@app.callback(
    Output('page-content', 'children'),
    [
        Input('url', 'pathname'),
    ]
)
def display_page(pathname):
    
    if pathname == '/':
        return gera_layout()
    elif pathname == '/apps_v01/page_1':
        return page_1.gera_layout()
    elif pathname == '/apps_v01/page_2':
        return page_2.gera_layout()
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)