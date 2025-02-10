# 🧀 Chasing Cheese 

## Introduction
A quick introduction, with use case, to Reinforcement Learning (Q-learn), used to solve the most classic problem for a mouse...find the cheese in the shortest way. 

##  📄 About the Q-learn & Bellman function
The Q-learn is one of the most famous reinforcement leraning algorithm. It's considered as a "model-free" algorithm, that means it does not require a model of the environment (hence "model-free"), and it can handle problems with stochastic transitions and rewards without requiring adaptations. In practice means that it will follow a probability matrix to describe the multiple situations (status). Q-learning finds an optimal policy in the sense of maximizing the expected value of the total reward over any and all successive steps, starting from the current state. 
"Q" refers to the function that the algorithm computes: the expected reward — that is, the _**Quality**_ — of an action taken in a given state.

What are the "main characters" of this procedure? This is what we need:
- an agent,
- a set of states (_S_),
- a set (_A_) of actions per state.

What they will do? 
1) By performing an action (a ∈ A), the agent transitions from state to state.
2) Executing an action in a specific state provides the agent with a reward (a numerical score).
3) The goal of the agent is to maximize its total reward. It does this by _adding the maximum reward attainable from future states to the reward for achieving its current state_, effectively influencing the current action by the potential future reward.

Let's go a little bit deeper into the algorithm's function!

### _Bellman Function_
- Before learning begins, ⁠Q⁠ is initialized to a possibly arbitrary fixed value (chosen by the programmer). Then, at each time _t_ the agent selects an action $A_t$, observes a reward $R_{t+1}$, enters a new state $S_{t+1} (that may depend on both the previous state $S_t$ and the selected action), and _Q_ is updated.
- The core of the Q-learning algorithm is the _Bellman function_:

```math
Q^{new}(S_t, A_t) \leftarrow (1-\underbrace{\alpha}_{\text{learning rate}}) \cdot Q(S_t, A_t) + \underbrace{\alpha}_{\text{learning rate}} \cdot (\underbrace{R_{t+1}}_{\text{reward}} + \underbrace{\gamma}_{\text{discount factor}} \cdot \underbrace{\max_a Q(S_{t+1}, a)}_{\text{estimate of optimal future value}}) 
```
- Where $R_{t+1} is the reward received when moving from the state $S_t$ to the state $S_{t+1}$, and α is the learning rate (0<α≤1).

### _Learning rate & Discount factor_

1) _Learning rate_: it determines the extent to which newly acquired information will overwrite old information. A factor of 0 would prevent the agent from learning, while a factor of 1 would cause the agent to only care about recent information.
2) _Discount factor_: it determines the importance of future rewards. A factor of 0 will make the agent "opportunistic" and cause it to consider only current rewards, while a factor tending to 1 will make the agent also attentive to the rewards that it will receive in the long-term future.

## 🏅 Labyrinth and Reward 
We will first start using a simple labyrinth with 10 possible positions (from 1 to 10). 


### Tools
- Python: Bellman function, Numpy.


##  🔧 Tasks

Find out some insights from different datasets.



