from chatbot.character import Character

async def get_response(id, chat):
    character = Character(id)
    response = character.receive_chat(chat)
    return {
	    "result": response
	}