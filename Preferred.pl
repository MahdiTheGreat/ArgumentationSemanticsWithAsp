
% Generate
{selected_arg(X):arg(X)}:-.
% the reason we didn't just use ' not selected_arg(X)' is because we would get unsafe error
not_selected_arg(X):-arg(X),not selected_arg(X).

% Test for preferred
% We again use the same lines we used in the Admissible program and that is because a preferred set has to be at first admissible 
% and in the next line we check if there exists an unselected argument that doesn't attack or is attacked by our selected arguments and 
% it also doesn't attack itself. This is because we are trying to find the maximal admissible sets and a set is admissible if it cannot be extended by another argument.
% If there is an unselected argument that has no conflict with our selected argument and also doesn't attack itself, 
% then it should be added to the set and when added, we again check if the set is admissible, by the previously defined integrity constraints.  
:- selected_arg(X),selected_arg(Y),att(X,Y).
defends_against(X,Y,Z):-arg(X),arg(Y),arg(Z),att(Z,Y),att(X,Z).
:-selected_arg(X),not_selected_arg(Z),att(Z,X),not 1{defends_against(Y,X,Z):selected_arg(Y)}.
:-not_selected_arg(X),not att(X,X),not 1{att(X,Y):selected_arg(Y)},not 1{att(Y,X):selected_arg(Y)}.

% Arguments
arg(1..4).
%arg(1).


% Attacks
att(1,2). 
att(1,4).  
att(2,1).
%att(1,1).

#show selected_arg/1.
%#show not_selected_arg/1. 
