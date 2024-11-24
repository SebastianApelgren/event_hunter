from langchain.utilities import GoogleSerperAPIWrapper
from langchain.agents import Tool
from Event import Event

class Tools:
    def add_to_calender(event):
        print(f"Added event: {event.name} to calender")
        
    def web_search(query):
        if query:
            return GoogleSerperAPIWrapper().search(query)
        else:
            return "Please provide a search query"

    def create_event(name, date, location, description):
        if name and date and location and description:
            return Event(name, date, location, description)
        else:
            return "Please provide all the details"

    tools = [
        Tool(name="add_to_calender", func=add_to_calender, description="Adds an event to users calender"),
        Tool(name="web_search", func=web_search, description="Searches the web for a query"),
        Tool(name="create_event", func=create_event, description="Creates an event")
    ]