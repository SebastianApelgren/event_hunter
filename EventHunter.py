from Models import *

class EventHelper:

    def __init__(self, agent):
        self.agent = agent

    def getChatResponse(self, query):
        response = self.agent.Invoke(query)
        return response
    