import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotnev()
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")


class LLMModel:
    def __init__(self,model_name="Gemma2-9b-It"):
        if not model_name:
            raise ValueError ("Model is not defined")
        self.model_name=model_name
        self.groq_model=ChatGroq(model=self.model_name)

    def get_model(self):
        return self.groq_model
    
    
    
if __name__=="__main__":
    llm_instance=LLMModel()
    llm_model=llm_instance.get_model()
    response=llm_model.invoke("hi")

    print(response)






















































