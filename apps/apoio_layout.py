from app import app

import dash_core_components as dcc
import dash_html_components as html

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                              Rotinas de Apoio
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def gera_rodape():

    return html.Div(
            [
                html.A(
                    [
                        html.Img(
                            # src= app.get_asset_url('image/'),
                            title='',
                            className='app__menu__img',
                        )
                    ],
                    href='#',
                    className='two columns',
                    style={'display': 'flex', 'justify-content': 'center'}
                ),

                html.A(
                    [
                        html.Img(
                            src= app.get_asset_url('image/github_PNG15.png'),
                            title='Perfil Pessoal no GitHub',
                            className='app__menu__img',
                        )
                    ],
                    href='https://github.com/Miguel-mmf',
                    className='two columns',
                    style={'display': 'flex', 'justify-content': 'center'}
                ),

                html.A(
                    [
                        html.Img(
                            # src= app.get_asset_url('image/'),
                            title='',
                            className='app__menu__img',
                        )
                    ],
                    href='#',
                    className='two columns',
                    style={'display': 'flex', 'justify-content': 'center'}
                ),

                html.A(
                    [
                        html.Img(
                            # src= app.get_asset_url('image/'),
                            title='',
                            className='app__menu__img',
                        )
                    ],
                    href='#',
                    className='two columns',
                    style={'display': 'flex', 'justify-content': 'center'}
                ),

                html.A(
                    [
                        html.Img(
                            # src= app.get_asset_url('image/'),
                            title='',
                            className='app__menu__img',
                        )
                    ],
                    href='#',
                    className='two columns',
                    style={'display': 'flex', 'justify-content': 'center'}
                ),

                html.A(
                    [
                        html.Img(
                            #src= app.get_asset_url('image/'),
                            title='',
                            className='app__menu__img',
                        )
                    ],
                    href='#',
                    className='two columns',
                    style={'display': 'flex', 'justify-content': 'center'}
                ),
            ],
            className='box_rodape',
            # style={'height':'30px', 'border-top': '1px solid rgb(139, 143, 167)'}
        )


def gera_button_return():

    return html.Div(
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
    ),

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                       Fim das Rotinas de Apoio
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++