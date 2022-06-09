from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from classes.ChatBot import ChatBot




app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def welcome():
    return {"message": "Welcome to Jina ML API"}


bot = ChatBot()
@app.post("/api/ml/code_esi_chatbot")
async def code_esi_chatbot(user_input: str):
    # for the terminal test
    return bot.get_result(user_input)

@app.get("/api/ml/code_esi_chatbot")
def code_esi_chatbot_get():
    return {"message": "code_esi_chatbot"}
