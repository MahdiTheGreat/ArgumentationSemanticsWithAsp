# Formulation of the problem
Formal argumentation is concerned primarily with reaching conclusions through logical reasoning, that is, claims based on premises. In the past few years, formal models of argumentation have been steadily gaining importance in artificial intelligence, where they have found a wide range of applications in specifying semantics for logic programs, decision-making, generating natural language text and supporting multi-agent dialogue, among others.

The conflicts between arguments have been modeled by directed graphs, which are called Argumentation Frameworks:

- An argumentation framework is a pair AF := ⟨AR,attacks⟩, where AR is a finite set of arguments, and attacks is a binary relation on AR, i.e. attacks ⊆ AR × AR.

We say that a attacks b (or b is attacked by a) if attacks(a,b) holds. Similarly, we say that a set S of arguments attacks b (or b is attacked by S) if b is attacked by an argument in S. We say that c defends a if b attacks a and c attacks b.

Let us observe that an AF is a simple structure which captures the conflicts of a given set of arguments. In order to select coherent points of view from a set of conflicts of arguments, the so-called argumentation semantics are used. These argumentation semantics are based on the concept of an admissible set:

- A set S of arguments is said to be conflict-free if there are no arguments a, b in S such that a attacks b.
- An argument a ∈ AR is acceptable with respect to a set S of arguments if and only if for each argument b ∈ AR: If b attacks a then b is attacked by S.
- A conflict-free set of arguments S is admissible if and only if each argument in S is acceptable w.r.t. S.

Considering admissible sets, two popular argumentation semantics for selecting arguments are the stable semantics and the preferred semantics which are defined as follows:

Let AF := ⟨AR,attacks⟩ be an argumentation framework. An admissible set of argument S ⊆ AR is.
- a stable extension of AF if S attacks each argument which does not belong to S.
- a preferred extension of AF if S is a maximal (with respect to set inclusion) admissible set of AF.

The stable semantic of AF is the set of stable extension of AF. The preferred semantics of AF is the set of preferred extensions of AF.

# Mission 

Implement  four different ASP programs:
- Program 1: Given an argumentation framework (AF), Program 1 computes the  conflict free sets of AF ,
- Program 2: Given an argumentation framework (AF), Program 2 computes the  admissible sets of AF,
- Program 3: Given an argumentation framework (AF), Program 3 computes the  stable extensions of AF.
- Program 4: Given an argumentation framework (AF), Program 4 computes the  preferred extensions of AF.

INPUTS: 
an argument framework denoted by the following predicates:

arg/1 denoting arguments, e.g. 
arg(a). arg(b).

att/2 denoting attacks between argument, e.g.
att(a,b).
att(b,a).

OUTPUTS:
selected_arg/1 denoting acceptable arguments, e.g.

selected_arg(a)

# ASP Vs. CSP in an Imperative Programming language
We use a Constraint Satisfaction Problem or CSP solver that computes the preferred semantics and compare the results. We run both the clingo preferred program and the CSP program on several argumentation frameworks, from one with one argument, then one with five arguments, next one with ten arguments, and finally one with twenty arguments, with the probability of an edge between two nodes being 0.95. We tried running the programs on 50 arguments, but with both ASP and CSP, the program kept running forever. The graph comparing the response times of ASP(red) and CSP(blue) can be seen below:

![image](https://github.com/MahdiTheGreat/ArgumentationSemanticsWithAsp/assets/47212121/6928d328-4995-49d2-881a-eddbf269e05a)

We can see comparable performances until ten arguments, but with twenty arguments CSP had a much worst response time than ASP. This is because ASP, similar to dynamic programming, tries to use memory to improve performance and reduce complexity, by considering every possible value for the fluents, considering every predicate value, grounding the program based on facts, and using caching, which in small problems is a very acceptable trade-off, however as the size of the input increases, the space complexity becomes absurd and the trade-off is not worth it, in which case CSP and methods like genetic algorithm have better performance since they don't require as much memory. This is especially important because computing power usually costs less than memory.
