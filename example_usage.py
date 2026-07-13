from client import AgentStructuredOutputEnforcerClient
client = AgentStructuredOutputEnforcerClient()
print(client.enforce('{"id": 1}', {"required": ["id"]}))