   ...:     agents[agent_counter]["id"] = agent_counter
   ...:     agent_counter += 1
   ...:     return agents[agent_counter - 1]
   ...: 
   ...: # RETRIEVE all
   ...: @app.get("/agents/")
   ...: def get_agents():
   ...:     return list(agents.values())
   ...: 
   ...: # RETRIEVE single
   ...: @app.get("/agents/{agent_id}")
   ...: def get_agent(agent_id: int):
   ...:     if agent_id not in agents:
   ...:         raise HTTPException(status_code=404, detail="Agent not found")
   ...:     return agents[agent_id]
   ...: 
   ...: # UPDATE
   ...: @app.put("/agents/{agent_id}")
   ...: def update_agent(agent_id: int, agent: Agent):
   ...:     if agent_id not in agents:
   ...:         raise HTTPException(status_code=404, detail="Agent not found")
   ...:     agents[agent_id].update(agent.dict())
   ...:     return agents[agent_id]
   ...: 
   ...: # DELETE
   ...: @app.delete("/agents/{agent_id}")
   ...: def delete_agent(agent_id: int):
   ...:     if agent_id not in agents:
   ...:         raise HTTPException(status_code=404, detail="Agent not found")
   ...:     deleted = agents.pop(agent_id)
   ...:     return {"message": "Agent deleted", "agent": deleted}
