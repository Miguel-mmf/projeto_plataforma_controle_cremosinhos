import dash

app = dash.Dash(
    __name__,
    title='Plataforma Cremosinhos',
    update_title="Updating...", # default
    meta_tags=[
        {
            'name': 'author',
            'content': 'Miguel Marques Ferreira'
        },
        {
            'name': 'description',
            'content': 'A Plataforma Cremosinhos é um projeto desenvolvido para auxiliar no controle de produtos e insumos.'
        },
        {
            'name': 'reply-to',
            'content': 'mmfmiguel17@gmail.com'
        },
        {
            'http-equiv': 'content-language',
            'content': 'pt-br'
        },
        {
            'name':'viewport',
            'content': 'width=device-width, initial-scale=1.0'
        }
    ],
    # suprimindo as exceções das callbacks para que caso utilize modificações dinâmicas do layout, não ocorra erros
    suppress_callback_exceptions=True
)

server = app.server

# dicionário auxiliar
app.dict_apps = {}