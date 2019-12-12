from typing import List, Text


class NoAgentFoundException(Exception):
    pass

class Agent(object):
    def __init__(self, name, skills, load):
        self.name = name
        self.skills = skills
        self.load = load

    def __str__(self):
        return "<Agent: {}>".format(self._name)


class Ticket(object):
    def __init__(self, id, restrictions):
        self.id = id
        self.restrictions = restrictions


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        return [a for a in agents if a.load < 3]

    def _fetch_agent(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        eligible_agents = (a for a in agents if set(a.skills).intersection(set(ticket.restrictions)))
        agent = next(eligible_agents, None)
        if agent is None:
            raise NoAgentFoundException
        else:
            return agent

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplementedError


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        filtered_agents = self._filter_loaded_agents(agents)
        sorted_agents = sorted(filtered_agents, key=lambda a: a.load)
        return self._fetch_agent(ticket, sorted_agents)


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        filtered_agents = self._filter_loaded_agents(agents)
        # agents should be sorted first by the number of skills they have
        # then by their load
        sorted_agents = sorted(filtered_agents, key=lambda a: (len(a.skills), a.load))
        return self._fetch_agent(ticket, sorted_agents)



def test_():
    ticket = Ticket(id="1", restrictions=["English"])
    agent1 = Agent(name="A", skills=["English"], load=2)
    agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)

    least_loaded_policy = LeastLoadedAgent()
    # returns the Agent with name "B" because of their currently lower load.
    ag = least_loaded_policy.find(ticket, [agent1, agent2])
    assert ag.name == "B"

    least_flexible_policy = LeastFlexibleAgent()
    # returns the Agent with name "A" because of their lower flexibility.
    ag = least_flexible_policy.find(ticket, [agent1, agent2])
    assert ag.name == "A"

def test_2():
    agent1 = Agent(name="A", skills=["English"], load=2)
    agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)
    ticket2 = Ticket(id="2", restrictions=["French"])

    least_flexible_policy = LeastFlexibleAgent()
    # returns the Agent with name "A" because of their lower flexibility.
    ag = least_flexible_policy.find(ticket2, [agent1, agent2])
    assert ag.name == "A"
