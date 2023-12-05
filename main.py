from clingo.control import Control
from constraint import *
from enum import Enum
import random
import time
import matplotlib.pyplot as plt
from csp_cython_solver import solver

def random_graph_generator(node_number,edge_prob=0.7):
    # graph = {1: [2, 4],
    #                   2: [1],
    #                   3: [],
    #                   4: []
    #                   }
    graph={}
    for i in range(1,node_number+1):
        graph[i]=[]
        for j in range(1,node_number+1):
            if random.random()>(1-edge_prob):
                graph[i].append(j)
    return graph

class Extension(Enum):
    conflict_free = "conflict_free"
    admissible = "admissible"
    preferred = "preferred"

def extension_constraint(*args):
    extension = args[-1]
    argument_graph = args[-2]
    argument_values = args[0:len(args) - 2]
    arguments = sorted(argument_graph.keys())
    selected_args = []
    for i in range(len(arguments)):
        if argument_values[i]: selected_args.append(arguments[i])
    extension_constraint_dict = {
        Extension.conflict_free: conflict_free_constraint,
        Extension.admissible: admissible_constraint,
        Extension.preferred: preferred_constraint
    }
    temp=extension_constraint_dict[extension]
    return temp(argument_graph, selected_args)


def conflict_free_constraint(argument_graph, selected_args):
    for arg1 in selected_args:
        for arg2 in selected_args:
            if not (arg1 in argument_graph[arg1]) and not (arg1 in argument_graph[arg2]) \
                    and not (arg2 in argument_graph[arg2]) and not (arg2 in argument_graph[arg1]):
                pass
            else:
                return False
    return True


def admissible_constraint(argument_graph, selected_args):
    if not conflict_free_constraint(argument_graph, selected_args):return False
    not_selected_args = set(argument_graph.keys()) - set(selected_args)
    for selected_arg in selected_args:
        for not_selected_arg in not_selected_args:
            if selected_arg in argument_graph[not_selected_arg]:
                defended = False
                for defender in selected_args:
                    if not_selected_arg in argument_graph[defender]: defended = True
                if defended:
                    pass
                else:
                    return False
    return True


def preferred_constraint(argument_graph, selected_args):
    if not admissible_constraint(argument_graph, selected_args):return False
    not_selected_args = set(argument_graph.keys()) - set(selected_args)
    for not_selected_arg in not_selected_args:
        threatening = False
        if not_selected_arg in argument_graph[not_selected_arg]: continue
        for selected_arg in selected_args:
            if not_selected_arg in argument_graph[selected_arg] or \
                    selected_arg in argument_graph[not_selected_arg]:
                threatening = True
        if not threatening: return False
    return True

generator_tester="""
% Generate
{selected_arg(X):arg(X)}:-.
% the reason we didn't just use ' not selected_arg(X)' is because we would get unsafe error
not_selected_arg(X):-arg(X),not selected_arg(X).

% Test for preferred
:- selected_arg(X),selected_arg(Y),att(X,Y).
defends_against(X,Y,Z):-arg(X),arg(Y),arg(Z),att(Z,Y),att(X,Z).
:-selected_arg(X),not_selected_arg(Z),att(Z,X),not 1{defends_against(Y,X,Z):selected_arg(Y)}.
:-not_selected_arg(X),not att(X,X),not 1{att(X,Y):selected_arg(Y)},not 1{att(Y,X):selected_arg(Y)}.

#show selected_arg/1.
"""

# argument_graph = {1: [2, 4],
#                   2: [1],
#                   3: [],
#                   4: []
#                   }

# argument_graph ={1: [1]}

# node_values=[10,20,50,100]
node_values=[10,20]
asp_times=[]
csp_times=[]

for node_value in node_values:
 argument_graph=random_graph_generator(node_value)
 # to make the list hashable, we use a tuple
 arguments = sorted(argument_graph.keys())

 ctl = Control()
 # we configure the control so that it enumerates over all the asnwers
 ctl.configuration.solve.models = 0
 # ctl.add("base", [], """\
 # p(@inc(10)).
 # q(@seq(1,2)).
 # """)
 ctl.add("base", [], generator_tester)
 instance=''
 instance+='arg('+str(arguments[0])+'..'+str(arguments[-1])+').'

 problem = Problem(BacktrackingSolver(forwardcheck=True))

 for argument in arguments:
     problem.addVariable(str(argument), [True, False])
     for attacked_arg in argument_graph[argument]:
      # the domain of variables have to be a list, even if the list has only one elemen
      instance += 'att(' + str(argument) + ',' + str(attacked_arg) + ').'


 ctl.add("base", [],instance)

 problem.addVariable('argument_graph', [argument_graph])
 problem.addVariable('Extension',[Extension.preferred])
 problem.addConstraint(
     extension_constraint
     , variables=[str(argument) for argument in arguments] + ['argument_graph'] + ['Extension']
 )
 start_time=time.time()
 ctl.ground([("base", [])])
 temp=ctl.solve(on_model=lambda m: print("Answer: {}".format(m)))
 asp_times.append(time.time()-start_time)

 start_time = time.time()
 # solutions = problem.getSolutions()
 solutions = solver(problem)
 csp_times.append(time.time() - start_time)
 for i in range(len(solutions)):
     del solutions[i]['argument_graph']
     del solutions[i]['Extension']
     solutions[i] = list(dict(filter(lambda pair: pair[1], solutions[i].items())).keys())
 print(solutions)
 print(len(solutions))

print("asp rsp times are"+str(asp_times))
print("csp rsp times are "+str(csp_times))
plt.legend(loc='best')
plt.plot(node_values, asp_times,label='ASP',color='r')
plt.plot(node_values, csp_times,label='CSP',color='b')
plt.title("ASP vs CSP rsp time", fontsize=20)
plt.xlabel("Arguments", fontsize=12)
plt.ylabel("Time(seconds)", fontsize=12)
plt.show()









