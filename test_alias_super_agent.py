import pytest
from alias_super_agent import Khalil7osniAlayoubiSuperAgent, BaseAgent

def test_agent_registration():
    alias = Khalil7osniAlayoubiSuperAgent()
    agent = BaseAgent("Test Agent")
    alias.register_agent(1, agent)
    assert len(alias.agents) == 1
    assert alias.agents[1] == agent

def test_monitor_agents(capsys):
    alias = Khalil7osniAlayoubiSuperAgent()
    agent1 = BaseAgent("Agent 1")
    agent2 = BaseAgent("Agent 2")
    agent3 = BaseAgent("Agent 3")  # Adding a third agent
    alias.register_agent(1, agent1)
    alias.register_agent(2, agent2)
    alias.register_agent(3, agent3)  # Registering the third agent
    
    alias.monitor_agents()
    captured = capsys.readouterr()
    print(captured.out)  # Debugging output
    assert "Agent 1 status: Idle" in captured.out
    assert "Agent 2 status: Idle" in captured.out
    assert "Agent 3 status: Idle" in captured.out  # Adding assertion for the third agent

def test_delegate_task(capsys):
    alias = Khalil7osniAlayoubiSuperAgent()
    agent = BaseAgent("Task Agent")
    agent2 = BaseAgent("Another Task Agent")  # Adding another agent
    alias.register_agent(1, agent)
    alias.register_agent(2, agent2)  # Registering the second agent
    
    alias.delegate_task(1, "Perform Task")
    captured = capsys.readouterr()
    print(captured.out)  # Debugging output
    assert "Task delegated to Agent 1." in captured.out
    assert agent.get_status() == "Executing Perform Task"
    assert agent2.get_status() == "Idle"  # Adding assertion for the second agent's status
