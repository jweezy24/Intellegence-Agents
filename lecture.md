---
title: "Intelligence Agents"
author: "Jack West"
bibliography: biblio.bib
link-citations: yes
---
# What are Agents?

 Jacques Ferber defines an agent as, " a physical or virtual entity that can act, perceive its environment (in a partial way) and communicate with others,is autonomous and has skills to achieve its goals and tendencies," [@z2]. In other words, an agent is usually given a set of tasks that it should solve. Those tasks are given in an environment that changes. The agent in question should adapt to those new changes. The agent's result should change when the environment changes. One agent is just a agent on a system. Where as if the system contains more than one agent the system is referred to as a "Multi-agent system"(MAS).

# Environments for Agents:

Agents are measured by their performance in the environment they were built for. Thus, there are a multitude of criteria a environment can be judged on. Agents are evaluated by how well they are able to manage the several pieces of their their environment. How the environment is described depends on how it fairs with five categories. We will first look at accessibility. All the categories below are defined firstly by Russel and Norvig [@HERE1].

### Accessibility
How accessible an agent is depends on its sensory apparatus. So accessibility is graded on how well the agent's sensors evaluate the environment. An agent that is built for all aspects of its environment means the environment is very accessible. You can look at accessibility as how well the agent interprets the environment. A human example of evaluating accessibility lies within Northwestern running-backs. Northwestern recruiters are known for picking a running-back that thinks before they run. Meaning, Northwestern running-backs are know for path finding. The way the runner evaluates their path is based on how well they deal with the data they are given. The recruiters look for how well the runner observes the field. Thus, a vital piece to a Northwestern running back is based on how well the runner deals with their sensory feedback. Thus, Northwestern recruiters look for a runner has high accessibility of the field. The best players that are accessible judge their environment quickly. Agents are judged on accessibility in the same sense. An agent's accessibility also depends on speed. The better the agent's sensors fair in a environment, the more accessible the environment.

### Determinism
Determinism describes how complex the environment is for the agent. A deterministic and accessible environment means that there is very little uncertainty. As in, there is very little space for random events to occur. Designing an agent for a highly deterministic and accessible environments are much easier than the non-deterministic types. Linear video games are a great example of highly deterministic environments. The word linear refers to the domino effect of events that are planned out. So, designing AI for these kinds of games tends to be easier than an open-ended game. When the developers know for a fact that the player will enter a room with a very similar level of progression; the AI has a much smaller set of scenarios to prepare for. Unlike when the game was open ended because open ended games have a level of randomness to them. A player can enter a level at anytime. Thus, the AI must be ready for all scenarios that could occur. Although, open ended games aren't the best counter example because any video game has finite planned events. A better example of a non-deterministic environment is the stock market. Anything in the human world can happen. Any agent, no matter how smart, will not be prepared for a Donald Trump tweet.

### Episodic
When looking how episodic an environment is we have to think of events as "episodes". Unlike television shows, these episodes are often completely separate with no overarching narrative the agent must prepare for. Meaning, a very episodic environment does not need to think ahead. If we relate these episodic events back to TV, a more episodic environment would be a situation comedy (sitcom). Each episode of a sitcom usually doesn't build off the last. The plot has to do with the situation of each episode. Just like with agents, the same logic applies. An entirely episodic environment though might not even share the same cast episode to episode.

### Static
A environment could be either static or dynamic. A static environment will not change while a agent is working, whereas a dynamic environment will change at any point in time. Static environments are much easier to deal with, as the agent no longer has to worry about the environment as it's working. Agents could queue up events as they come in and only have to check the environment before and after dealing with an event.If the environment does not change with the passage of time but the agent does, we call that semidynamic.

### Discrete
How discrete an environment is how many events are possible within the environment. The opposite of discrete environment is a continuous environment. It sounds similar to to determinism but determinism discusses the complexity of the situation rather than the events that the situation embodies. For example, video games are deterministic and discrete. Although, when the players are pinned against each other the game can become continuous. One type of game that is very continuous in nature are fighting games. Their environments are very deterministic. As in, the rules within a fighting game's environment are simple and will not change. Actually playing the game against a person is a different story. A human player can do something completely out of left field that even with years of experience and practice one may still be caught off guard. Where as a game like chess is very discrete. The set of possible scenarios is finite. Making chess more discrete.

# Designing for Environments

## Simple Environments
![Figure 1](/images/basicDesign.png)
[@z3]

Environments can range from being as simple as reacting to a packet or can be as complex as reacting to the stock market. Agents are made to deal with specific environments. Most agents will be designed like the diagram above. The figure above is suited for a environment that is very discrete, static, deterministic, episodic, and accessible. You can see how linear the process is for a simple agent. In the most simple situation the system would only need a single agent waiting in a thread.

## Complex Environments
[Figure 2]: /images/complexDesign.png
![logo][Figure 2]


The image above describes a agent that adapts to its environment as it is read in. As you can see there is a lot more going on. For one, the simple diagram doesn't have to be multi-threaded. Where as, the complex diagram has to be multi-threaded if the user wishes to have fast and accurate results. Also, what is commonly done with a complex environment is multiple agents will be needed thus the system will become a MAS. So complex environments need more from agents. Thus, to deal with a dynamic, continuous, non-deterministic environment. We need to observe what is commonly referred to as an intelligence agent.

# Intelligence Agents
Intelligence agents (also called rational agents), are agents that should be able to process any sequence of events with the highest speed and efficiency. The key part of a intelligence agent is the artificial intelligence aspects of dealing with a situation. How the agent adapts to a complex dynamic environment is what makes the agent in question intelligent.

There are two parts of the definition of a intelligence agents that we have to define separately. The first is the speed portion. Agents are able to get this performance by being an ideal agent. Ideal agents are agents that map new input to old output based on prior results. This is similar to a cache but with more logic. Ideal agents can also be intelligent as well. For example, if the mapping the agent is doing requires logical context then the agent is also intelligent. By logical context, I am referring to infinite sets of events. Obviously if the amount of possibilities are infinite one can not run code on that set. Infinite sets need to be approached logically if one could pull any data out of it. We call agents that are both intelligent and map values to a table are intelligent ideal agents(IIA). We care about ideal agents because they are there for performance boosts.

We've mentioned a few times about the agents being able to think on their own. Now we are going to define what that means. To be able to think on their own. The system of agents has to be autonomous. If we look back at [Figure 2], the autonomous part of the system I described is the adapt entity. That would serve as doing things autonomously.

# How are Intelligence Agents Distributed?
To really understand why intelligence agents are distributed, we should make a small example. A common situation for a simple intelligent agent to exist. A simple agent should take data and give results back based on the environment they were built for. We will be using python to develop a agent. When we give that agent a string of numbers, it should be able to make a linear equation based on the set of numbers. Although simple, this example we will be focusing on what makes the code distributed.
```python
import socket
import matplotlib.pyplot as plt
import json

class agent:
    def __init__(self,port):
        #initializes udp listener socket
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #initializes udp sender
        self.sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #gives socket a port and an ip address to bind to
        #we assign a port so that the environment knows where
        #to send the packet
        self.listener.bind(('', port))
        self.plot = plt

    #method to listen for packets
    def listen(self):
        #listens for packet
        message, address = self.listener.recvfrom(1024)
        #after receiving packet translates it
        self.translate(message,address)

    #translates the packet to be put on a graph
    def translate(self,message,address):
        #we are sending json packets.
        #to grab the data in the packets we use the python json library to read
        #the information
        points = json.loads(message)['points']
        #we are now plotting the line on a grid
        #sends a success message to the environment
        self.plot.plot([points[0],points[2]], [points[1],points[3]], 'ro-')
        #this will tell the environment know we are ready for the next line to make
        self.sender.sendto("success".encode(), address)

    #displays the graph
    def show(self):
        self.plot.show()
```   
As you can see from the example above, the agent class is going to be used in a distributed manner. A agent will be alive waiting for a job that will be given by the environment. We will make the environment next.
```python
import socket
import random
import json

class environment:
    #initalizes communication
    def __init__(self,ports):
        #initalizes udp listener socket
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #initalizes udp sender
        self.sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #making the socket a broadcast socket so that we don't need to know the ip of agent
        self.sender.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sender.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        #gives socket a port and an ip address to bind to
        self.listener.bind(('', 0))
        self.ports = ports

    def make_numbers(self):
        num1 = random.randint(0,10)
        num2 = random.randint(0,10)
        num3 = random.randint(0,10)
        num4 = random.randint(0,10)
        #creating json dictionary to be sent later
        json_dict = {"points":[num1,num2,num3,num4]}
        json_message = json.dumps(json_dict)
        #if there is only one port just send it there
        if type(self.ports) != type([]):
            self.sender.sendto(json_message.encode(), ('', self.ports))
        else:
            #if multiple ports exist send it there
            for i in self.ports:
                self.sender.sendto(json_message.encode(), ('', i))

```
The environment above is defined to send randomly generated numbers. Obviously there is little purpose to what we are making. The code we are writing is going to demonstrate more the distributed aspects. Agents are usually written in a distributed environment. Due to not wanting to make the code unusable without two machines, it will be able to run locally on one machine or on multiple machines. There won't be any learning. As the job the agents are working to solve have only one rule and the environment won't change. The purpose of the example is to show, even a simple agent has a distributed design. An intense algorithm that is meant to adapt and learn is something that even setting up an environment is needlessly complicated and specific. Even if we worked through a complex example, there would be little to no carry over for the amount of work it'll take to complete a complex example. Understanding the distributed aspects will make it easier to build off of.  
