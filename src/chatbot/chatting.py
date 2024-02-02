from character import Character
import streamlit as st
import os
import json

def character_page(file_path, user, relation, situation, content, new_situation):
    st.title("Fiction Comes True")
    
    # elif 조건: 사용자 캐릭터 바꿀 때 봇 대사 업데이트 안 되는 문제 해결하기 위함
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": content}]
    elif len(st.session_state.messages) == 1:
        st.session_state.messages = [{"role": "assistant", "content": content}]

    # 스토리 전개를 위해 추가한 부분. 5번 이상 대화를 주고받으면 상황이 바뀐다. 
    if len(st.session_state.messages) > 5:
        overall_chain = Character(file_path, user, relation, new_situation)
    else:
        overall_chain = Character(file_path, user, relation, situation)
    
    # 지금까지 대화한 것 보여 주기
    for message in st.session_state.messages:
        st.chat_message(message["role"]).write(message["content"])
    
    # 대화 UI
    if prompt := st.chat_input("캐릭터에게 할 말을 입력하세요."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        # 사용자 인풋 보여 주기
        with st.chat_message("user"):
            st.markdown(prompt)
        # 봇 대답 보여 주기
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            assistant_response = overall_chain.receive_chat(prompt)
            message_placeholder.markdown(assistant_response)
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        
    # 지금까지 진행한 대화 json 파일로 저장하기(요약에 넣어 줌)
    save_conversation_to_json(st.session_state.messages, "data/conversation.json")

# 대화 기록을 json 파일로 저장하는 함수
def save_conversation_to_json(messages, filename):
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(messages, json_file, ensure_ascii=False, indent=4)        

def main():
    os.environ["OPENAI_API_KEY"] = st.secrets["openai_key"]
    
    st.sidebar.title("캐릭터 선택")
    
    with open("data/situation.json", "r", encoding="utf-8") as f:
        json_data = f.read()
    
    situation_data = json.loads(json_data)
    
    selected_char = st.sidebar.selectbox(
        "대화할 캐릭터를 선택하세요.",
        ["선택", "백설공주", "겨울왕국 엘사", "파워퍼프걸 블로섬", "신의 탑 밤", "나루토", "원피스 루피"]
    )
    
    if selected_char == "백설공주":
        user_char = st.sidebar.selectbox(
            "사용자 캐릭터를 선택하세요.",
            ["마녀", "난쟁이"]
        )
        
        if user_char == "마녀":
            # 봇 캐릭터 - 사용자 캐릭터 연결 순서대로 감(스트림릿에서 이거 노가다 안 하는 법 모르겠어서 이렇게 둠 ㅎㅎ)
            sit_data = situation_data[0]
            selected_sit = st.sidebar.selectbox(
                "대화할 상황을 선택하세요.",
                [sit_data["sit_title"]]
            )
            user = sit_data["user"]
            relation = sit_data["relation"]
            situation = sit_data["sit_prompt"]
            content = sit_data["sit_line"]
            new_situation = sit_data['new_prompt']
            character_page("data/snow_white.json", user, relation, situation, content, new_situation)
        
        if user_char == "난쟁이":
            sit_data = situation_data[1]
            selected_sit = st.sidebar.selectbox(
                "대화할 상황을 선택하세요.",
                [sit_data["sit_title"]]
            )
            user = sit_data["user"]
            relation = sit_data["relation"]
            situation = sit_data["sit_prompt"]
            content = sit_data["sit_line"]
            new_situation = sit_data['new_prompt']
            character_page("data/snow_white.json", user, relation, situation, content, new_situation)
        
    if selected_char == "겨울왕국 엘사":
        user_char = st.sidebar.selectbox(
            "사용자 캐릭터를 선택하세요.",
            ["안나"]
        )
        
        if user_char == "안나":
            sit_data = situation_data[2]
            selected_sit = st.sidebar.selectbox(
                "대화할 상황을 선택하세요.",
                [sit_data["sit_title"]]
            )
            user = sit_data["user"]
            relation = sit_data["relation"]
            situation = sit_data["sit_prompt"]
            content = sit_data["sit_line"]
            new_situation = sit_data['new_prompt']
            character_page("data/elsa.json", user, relation, situation, content, new_situation)
    
    if selected_char == "파워퍼프걸 블로섬":
        user_char = st.sidebar.selectbox(
            "사용자 캐릭터를 선택하세요.",
            ["버블", "버터컵"]
        )
        
        if user_char == "버블":
            sit_data = situation_data[3]
            selected_sit = st.sidebar.selectbox(
                "대화할 상황을 선택하세요.",
                [sit_data["sit_title"]]
            )
            user = sit_data["user"]
            relation = sit_data["relation"]
            situation = sit_data["sit_prompt"]
            content = sit_data["sit_line"]
            new_situation = sit_data['new_prompt']
            character_page("data/blossom.json", user, relation, situation, content, new_situation)
        
        if user_char == "버터컵":
            sit_data = situation_data[4]
            selected_sit = st.sidebar.selectbox(
                "대화할 상황을 선택하세요.",
                [sit_data["sit_title"]]
            )
            user = sit_data["user"]
            relation = sit_data["relation"]
            situation = sit_data["sit_prompt"]
            content = sit_data["sit_line"]
            new_situation = sit_data['new_prompt']
            character_page("data/blossom.json", user, relation, situation, content, new_situation)
    
    if selected_char == "신의 탑 밤":
        user_char = st.sidebar.selectbox(
            "사용자 캐릭터를 선택하세요.",
            ["쿤", "엔도르시"]
        )
        
        if user_char == "쿤":
            sit_data = situation_data[5]
            selected_sit = st.sidebar.selectbox(
                "대화할 상황을 선택하세요.",
                [sit_data["sit_title"]]
            )
            user = sit_data["user"]
            relation = sit_data["relation"]
            situation = sit_data["sit_prompt"]
            content = sit_data["sit_line"]
            new_situation = sit_data['new_prompt']
            character_page("data/bam.json", user, relation, situation, content, new_situation)
        
        if user_char == "엔도르시":
            sit_data = situation_data[6]
            selected_sit = st.sidebar.selectbox(
                "대화할 상황을 선택하세요.",
                [sit_data["sit_title"]]
            )
            user = sit_data["user"]
            relation = sit_data["relation"]
            situation = sit_data["sit_prompt"]
            content = sit_data["sit_line"]
            new_situation = sit_data['new_prompt']
            character_page("data/bam.json", user, relation, situation, content, new_situation)
    
    if selected_char == "나루토":
        user_char = st.sidebar.selectbox(
            "사용자 캐릭터를 선택하세요.",
            ["사스케"]
        )
        
        if user_char == "사스케":
            sit_data = situation_data[7]
            selected_sit = st.sidebar.selectbox(
                "대화할 상황을 선택하세요.",
                [sit_data["sit_title"]]
            )
            user = sit_data["user"]
            relation = sit_data["relation"]
            situation = sit_data["sit_prompt"]
            content = sit_data["sit_line"]
            new_situation = sit_data['new_prompt']
            character_page("data/naruto.json", user, relation, situation, content, new_situation)
    
    if selected_char == "원피스 루피":
        user_char = st.sidebar.selectbox(
            "사용자 캐릭터를 선택하세요.",
            ["나미"]
        )
        
        if user_char == "나미":
            sit_data = situation_data[8]
            selected_sit = st.sidebar.selectbox(
                "대화할 상황을 선택하세요.",
                [sit_data["sit_title"]],
            )
            user = sit_data["user"]
            relation = sit_data["relation"]
            situation = sit_data["sit_prompt"]
            content = sit_data["sit_line"]
            new_situation = sit_data['new_prompt']
            character_page("data/luffy.json", user, relation, situation, content, new_situation)
        

if __name__ == "__main__" : 
    main()