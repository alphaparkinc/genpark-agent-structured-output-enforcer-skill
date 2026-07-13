class AgentStructuredOutputEnforcerClient:
    def enforce(self, json_output: str, schema: dict) -> dict:
        import json
        try:
            data = json.loads(json_output)
            return {"is_valid": all(k in data for k in schema.get("required", []))}
        except:
            return {"is_valid": False}