import json
from openai import OpenAI
import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class Summary:
    def __init__(self, chatting_file, id):
        self.chatting_file = chatting_file
        
        with open("chatbot/data/situation.json", "r", encoding="utf8") as json_file:
            json_data = json_file.read()
        self.data = json.loads(json_data)
        situation = self.data[id]['sit_prompt']
        print(situation)
        self.situation = situation
        self.id = id
    
    def summary(self):
        # with open(self.chatting_file, "r", encoding="utf8") as json_file:
        #     json_data = json_file.read()
        #     chatting_data = json.loads(json_data)
        chatting_data = self.chatting_file
        
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Summarize the following conversation with the given situation."},
                {"role": "user", "content": "Do not use word 'Bot' or 'User' in the summary. Just use character name."},
                {"role": "user", "content": "I will user that summarization for image generation. Make the summary as stable diffusion model prompt."},
                {"role": "user", "content": "Summarize whole context in 50 tokens, and wrote in English."},
                {"role": "user", "content": "Divide the summarized situation into two parts and present it in the form 1. and 2."},
                {"role": "user", "content": "The Example of summary is: 1. naruto, 1boy, solo, male focus, blue eyes, facial mark, looking at viewer / 2. smiling, orange jacket, jacket, closed mouth. You should follow this format."},
                {"role": "user", "content": "The Example of summary is: 1. Endorsi, confessing love, sincerely / 2. Bam, accepting love, shyly"},
                {"role": "user", "content": "Do not use \n in the summary. Just use / to divide the summary."},
                {"role": "assistant", "content": "Yes."},
                {"role": "user", "content": str(chatting_data)},
                {"role": "user", "content": self.situation}
            ],
        )
        
        sum = str(response.choices[0].message.content)
        
        sum1 = sum.split("/")[0]
        sum2 = sum.split("/")[1]
        
        sum1 = sum1.replace("1. ", "")
        sum2 = sum2.replace("2. ", "")
        sum2 = sum2.replace("\n", "")
        
        data = {"bot": self.data[self.id]['bot'], "user": self.data[self.id]['user'], "summary": [sum1, sum2]}
        
        return data

def main():
    with open("data/situation.json", "r", encoding="utf8") as json_file:
        json_data = json_file.read()
        sit_data = json.loads(json_data)
        sit_data = sit_data[6]
    
    sum = Summary("data/conversation.json", 0)
    sum = str(sum.summary())
    
    sum1 = sum.split("/")[0]
    sum2 = sum.split("/")[1]
    
    sum1 = sum1.replace("1. ", "")
    sum2 = sum2.replace("2. ", "")
    sum2 = sum2.replace("\n", "")
    
    data = {"bot": sit_data['bot'], "user": sit_data['user'], "summary": [sum1, sum2]}
    
    with open("src/data/image.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4) 

if __name__ == "__main__":
    main()