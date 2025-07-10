


from flask import Flask
from flasgger import Swagger
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
swagger = Swagger(app)

# Importa e registra as rotas customizadas
from routes import routes
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)
