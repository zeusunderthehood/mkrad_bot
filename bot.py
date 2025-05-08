from langgraph.graph import StateGraph,MessagesState,START,END
from langgraph.graph.message import add_messages
from typing import TypedDict,Annotated,Sequence,Optional
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"]=os.getenv('GROQ_API_KEY')
from pydantic import BaseModel,Field
from database import UserFetchFormat
import operator
model="Llama3-8b-8192"
llm=ChatGroq(model=model)


class AgentState(TypedDict):
    messages:Annotated[Sequence[BaseMessage],operator.add]
    phone: Optional[str]
    user: Optional[dict]
    user_exists: Literal[True, False, None]
        
        
        
        
        
        
        