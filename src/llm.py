import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from src.config import instruction

load_dotenv() #load all our environment variables

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

def ask_bot(user_message,instruction):
    
    model = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)
    
    response=model(
    [
        SystemMessage(content=instruction),
        HumanMessage(content=user_message),
    ]
) 
    return response.content


if __name__ == "__main__":
    user_message = "Hii, how are you?"
    reponse = ask_bot(user_message)
    print(reponse)