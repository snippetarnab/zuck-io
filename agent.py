class AIAgent:                                        
    def __init__(self, api_key: str):                 
        self.client = Anthropic(api_key=api_key)      
        self.messages: List[Dict[str, Any]] = []      
        self.tools: List[Tool] = []                   
        print("Agent initialized")   