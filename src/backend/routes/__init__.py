# Pasta para rotas customizadas

from flask import Blueprint, request, jsonify

routes = Blueprint('routes', __name__)

@routes.route('/api/chat', methods=['POST'])
def chat():
    """
    Recebe uma mensagem do frontend e retorna uma resposta simples.
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            message:
              type: string
    responses:
      200:
        description: Resposta do chatbot
        schema:
          type: object
          properties:
            response:
              type: string
    """
    data = request.get_json()
    user_message = data.get('message', '')
    # Lógica simples de resposta
    if not user_message.strip():
        bot_response = 'Por favor, envie uma mensagem.'
    elif 'oi' in user_message.lower():
        bot_response = 'Olá! Como posso ajudar você?'
    else:
        bot_response = f'Você disse: {user_message}'
    return jsonify({'response': bot_response})
