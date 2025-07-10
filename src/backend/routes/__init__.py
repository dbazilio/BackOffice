# Pasta para rotas customizadas


from flask import Blueprint, request, jsonify
import json
import os
from datetime import datetime
from .chatbot_logic import ChatbotLogic

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
    # Lógica de resposta centralizada na classe ChatbotLogic
    bot_response = ChatbotLogic.get_response(user_message)

    # Caminho do arquivo JSON
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'FakeDataBase', 'chats.json')
    db_path = os.path.abspath(db_path)

    # Carrega os dados existentes
    try:
        with open(db_path, 'r', encoding='utf-8') as f:
            chats_data = json.load(f)
    except Exception:
        chats_data = {"chats": []}

    # Gera novo id
    new_id = (chats_data["chats"][-1]["id"] + 1) if chats_data["chats"] else 1
    # Adiciona nova conversa
    chats_data["chats"].append({
        "id": new_id,
        "user_message": user_message,
        "bot_response": bot_response,
        "timestamp": datetime.utcnow().isoformat() + 'Z'
    })

    # Salva de volta no arquivo
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(chats_data, f, ensure_ascii=False, indent=2)

    return jsonify({'response': bot_response})


# Endpoint para buscar o histórico de conversas
@routes.route('/api/chats', methods=['GET'])
def get_chats():
    """
    Retorna o histórico de conversas salvas no banco de dados mockado.
    ---
    responses:
      200:
        description: Lista de conversas
        schema:
          type: object
          properties:
            chats:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  user_message:
                    type: string
                  bot_response:
                    type: string
                  timestamp:
                    type: string
    """
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'FakeDataBase', 'chats.json')
    db_path = os.path.abspath(db_path)
    try:
        with open(db_path, 'r', encoding='utf-8') as f:
            chats_data = json.load(f)
    except Exception:
        chats_data = {"chats": []}
    return jsonify(chats_data)
