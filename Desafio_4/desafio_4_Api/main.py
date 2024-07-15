from fastapi import FastAPI
from desafio_4_Api.routers import api_router

app = FastAPI(title='Desafio_4_Api')
app.include_router(api_router)

# - adicionar query parameters nos endpoints
#     - atleta
#         - nome
#         - cpf
# - customizar response de retorno de endpoints
#     - get all
#         - atleta
#             - nome
#             - centro_treinamento
#             - categoria
# - Manipular exceção de integridade dos dados em cada módulo/tabela
#     - sqlalchemy.exc.IntegrityError e devolver a seguinte mensagem: “Já existe um atleta cadastrado com o cpf: x”
#     - status_code: 303
# - Adicionar paginação utilizando a lib: fastapi-pagination
#     - limit e offset