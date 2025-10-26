
"""
Bayesian inference in Python involves using the principles of Bayes' Theorem to update the probability of a
hypothesis as new evidence becomes available. Several Python libraries facilitate this process, each offering
different approaches and levels of complexity.

Key Libraries for Bayesian Inference in Python:

PyMC: A powerful and widely used library for probabilistic programming, enabling users to build and infer from
Bayesian models using various sampling methods like Markov Chain Monte Carlo (MCMC). It's built on a flexible
backend and supports advanced features like GPU acceleration.
ArviZ: A library for exploratory analysis of Bayesian models, offering tools for visualization, diagnostics, and
model comparison, often used in conjunction with PyMC.
Bambi: A high-level interface for PyMC, simplifying the process of fitting Bayesian regression models by providing
a familiar R-like syntax.
BayesPy: Focuses on variational Bayesian inference for conjugate-exponential family models, offering an efficient
 approach to approximate posterior distributions.
PyVBMC: Implements Variational Bayesian Monte Carlo (VBMC), a sample-efficient algorithm for Bayesian inference,
particularly useful for models with expensive likelihood evaluations.
BayesicFitting: A toolbox designed for Bayesian fitting and evidence calculation, providing a standardized way to
 perform Bayesian inference, optimize parameters, and compare models.

Core Concepts in Bayesian Inference:
Prior Probability: Represents the initial belief about a hypothesis before observing any data.
Likelihood: The probability of observing the data given a specific hypothesis.
Posterior Probability: The updated probability of the hypothesis after considering the observed data, calculated
using Bayes' Theorem:
Code

    P(Hypothesis | Data) = [P(Data | Hypothesis) * P(Hypothesis)] / P(Data)
where P(Data) is the marginal likelihood or evidence.

Practical Application:
These libraries enable users to define probabilistic models, specify prior distributions for parameters, incorporate
observed data through likelihood functions, and then use inference algorithms (like MCMC or variational inference)
to approximate the posterior distributions of the parameters.
This allows for quantifying uncertainty, making predictions, and comparing different models based on their evidence.

ai----------------
The pomegranate library in Python provides tools for building and performing inference with probabilistic models,
including Bayesian networks. Bayesian inference in pomegranate primarily involves constructing a Bayesian network
and then using its predict_proba method to calculate conditional probabilities or beliefs given observed evidence.
Here's a breakdown of how to perform Bayesian inference using pomegranate:

1. Define Distributions for Nodes:
Each node in your Bayesian network needs an associated probability distribution. pomegranate offers various
distributions, such as DiscreteDistribution for categorical variables and NormalDistribution for continuous variables.
Python

from pomegranate import DiscreteDistribution, State, BayesianNetwork

# Define distributions for individual nodes
guest_dist = DiscreteDistribution({'A': 1./3, 'B': 1./3, 'C': 1./3})
prize_dist = DiscreteDistribution({'A': 1./3, 'B': 1./3, 'C': 1./3})
2. Create States:
Wrap each distribution in a State object, giving it a name for easy identification within the network.
Python

s_guest = State(guest_dist, name="Guest")
s_prize = State(prize_dist, name="Prize")
3. Define Conditional Probability Tables (CPTs) for Dependent Nodes:
For nodes that depend on other nodes, you need to define their conditional probabilities using
ConditionalProbabilityTable. This table specifies the probability of a child node's state given the states
of its parent nodes.
Python

from pomegranate import ConditionalProbabilityTable

# Example for a 'Monty' node dependent on 'Guest' and 'Prize'
monty_cpt = ConditionalProbabilityTable([
    ['A', 'A', 'B', 0.5], ['A', 'A', 'C', 0.5], # If guest chooses A, prize is A, Monty can open B or C
    ['A', 'B', 'C', 1.0], # If guest chooses A, prize is B, Monty must open C
    # ... and so on for all combinations
], [s_guest, s_prize])
s_monty = State(monty_cpt, name="Monty")
4. Build the Bayesian Network:
Instantiate a BayesianNetwork and add the states and edges (dependencies) between them.
Python

network = BayesianNetwork("Monty Hall Problem")
network.add_states(s_guest, s_prize, s_monty)
network.add_edge(s_guest, s_monty)
network.add_edge(s_prize, s_monty)
network.bake() # Prepare the network for inference
5. Perform Inference:
Use the predict_proba method to calculate the posterior probabilities of unobserved variables given some evidence.
Python

# Observe that the guest chose door 'A' and Monty opened door 'B'
beliefs = network.predict_proba({'Guest': 'A', 'Monty': 'B'})

# The `beliefs` object will contain the updated distributions for all nodes,
# including the posterior probability of the 'Prize' location.
By following these steps, you can effectively use pomegranate to model and perform Bayesian inference on various
 probabilistic scenarios.


"""
from pomegranate import DiscreteDistribution, State, BayesianNetwork
from pomegranate import ConditionalProbabilityTable



#---------------------------

# Define starting probabilities
# rain node has no parents
# rain node following this distribution
rain =Node(DiscreteDistribution({
    "none": 0.7,
    "light": 0.2,
    "heavy": 0.1
}), name = "rain")

# Define transition model
#track maintenance node is conditional on rain
maintenance = Node(ConditionalProbabilityTable([  #maintenance node follows this conditional probability distribution
    ["none", "yes", 0.4],
    ["none", "no", 0.6],
    ["light", "yes", 0.2],
    ["light", "no", 0.8],
    ["heavy", "yes", 0.1],
    ["heavy", "no", 0.9]
], [rain.distribution]), name = "maintenance")

# Train node is conditional on rain and maintenance
train = Node(ConditionalProbabilityTable([
    ["none", "yes", "on time", 0.8],
    ["none", "yes", "delayed", 0.2],
    ["none", "no", "on time", 0.9],
    ["none", "no", "delayed", 0.1],
    ["light", "yes", "on time", 0.6],
    ["light", "yes", "delayed", 0.4],
    ["light", "no", "on time", 0.7],
    ["light", "no", "delayed", 0.3],
    ["heavy", "yes", "on time", 0.4],
    ["heavy", "yes", "delayed", 0.6],
    ["heavy", "no", "on time", 0.5],
    ["heavy", "no", "delayed", 0.5],
], [rain.distribution, maintenance.distribution]), name="train")

# Appointment node is conditional on train
appointment = Node(ConditionalProbabilityTable([
    ["on time", "attend", 0.9],
    ["on time", "miss", 0.1],
    ["delayed", "attend", 0.6],
    ["delayed", "miss", 0.4]
], [train.distribution]), name="appointment")

# Create a Bayesian Network and add states
model = BayesianNetwork()
model.add_states(rain, maintenance, train, appointment)

# Add edges connecting nodes
model.add_edge(rain, maintenance)
model.add_edge(rain, train)
model.add_edge(maintenance, train)
model.add_edge(train, appointment)

# Finalize model
model.bake()







