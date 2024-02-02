import json
from openai import OpenAI
import os

class Summary:
    def __init__(self, chatting_file, situation):
        self.chatting_file = chatting_file
        self.situation = situation
    
    def summary(self):
        with open(self.chatting_file, "r", encoding="utf8") as json_file:
            json_data = json_file.read()
            chatting_data = json.loads(json_data)
        
        client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Summarize the following conversation with the given situation."},
                {"role": "user", "content": "Do not use word 'Bot' or 'User' in the summary. Just use character name."},
                {"role": "user", "content": "I will user that summarization for image generation. Make the summary as stable diffusion model prompt."},
                {"role": "user", "content": "Summary whole context in 50 tokens, and wrote in English."},
                {"role": "user", "content": "The Example of summary is: naruto, 1boy, solo, male focus, blue eyes, facial mark, looking at viewer, smiling, orange jacket, jacket, closed mouth. You should follow this format."},
                {"role": "user", "content": "The Example of summary is:  wanostyle, monkey d luffy, smiling, straw hat, looking at viewer, solo, upper body. You should follow this format."},
                {"role": "assistant", "content": "Yes."},
                {"role": "user", "content": str(chatting_data)},
                {"role": "user", "content": self.situation}
            ],
        )
    
        return response.choices[0].message.content

def main():
    with open("src/data/situation.json", "r", encoding="utf8") as json_file:
        json_data = json_file.read()
        sit_data = json.loads(json_data)
        sit_data = sit_data[0]
    
    sum = Summary("src/data/conversation.json", sit_data['sit_prompt'])
    data = {"bot": sit_data['bot'], "user": sit_data['user'], "summary": str(sum.summary())}
    
    with open("src/data/image.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4) 

if __name__ == "__main__":
    main()