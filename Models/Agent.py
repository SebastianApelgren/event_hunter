import json
from langchain.agents import AgentExecutor, create_structured_chat_agent

class Agent:

    def __init__(self, llm, tools, template):
        agent = create_structured_chat_agent(
            tools=tools,
            llm=llm,
            prompt=template,
        )
        self.agent_executor = AgentExecutor(agent, tools=tools, verbose=True)

    
    def invoke(self, query):
        response = self.agent_executor.invoke(query)
        return json.dumps({'response': response["output"]})
    
