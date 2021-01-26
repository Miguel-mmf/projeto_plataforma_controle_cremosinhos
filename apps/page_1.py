import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app
from apps import apoio_layout

if 'app_page_1' not in app.dict_apps:
    app.dict_apps['app_page_1'] = {}

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                              Rotinas de Apoio
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def gera_layout():
    
    return html.Div(
        [
            html.Div(
                [
                    dcc.Link(
                        'página principal',
                        title='Retornar para a página principal',
                        href='/',
                        className=' button button_return alinhamento_centro',
                    )
                ],
                className='wind__speed__container subtitle_style',
                style={'textAlign':'center','height':'40px'}
            )
        ]
    )

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                       Fim das Rotinas de Apoio
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++ CALLBACKS  ++++++++++++++++
