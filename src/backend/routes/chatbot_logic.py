class ChatbotLogic:
    @staticmethod
    def get_response(user_message: str) -> str:
        if not user_message.strip():
            return 'Por favor, envie uma mensagem.'
        elif 'oi' in user_message.lower():
            return 'Olá! Como posso ajudar você?'
        elif 'horário' in user_message.lower():
            return 'Nosso horário de funcionamento é das 9h às 18h, de segunda a sexta.'
        else:
            return f'Você disse: {user_message}'
