% Generate
{selected_arg(X):arg(X)}:-.
% the reason we didn't just use ' not selected_arg(X)' is because we would get unsafe error
not_selected_arg(X):-arg(X),not selected_arg(X).

% Test for admissible
% We again use the same line we used in the Conflict-free program and that is because an admissible set has to be at first conflict-free 
% and in the next lines we use the predicate "defeneds_againts(X,Y,Z)", which checks if the argument X defeneds the argument Y against the argument Z,
% i.e Z attacks Y and in turn X attacks Z. In the last line, we check if there is an unselected argument that attacks one of our selected arguments, 
% in a way that there is nobody to defend the said selected argument, and therefore the set of selected arguments is not admissible and its arguments are not acceptable w.r.t. S.
:- selected_arg(X),selected_arg(Y),att(X,Y).
defends_against(X,Y,Z):-arg(X),arg(Y),arg(Z),att(Z,Y),att(X,Z).
:-selected_arg(X),not_selected_arg(Z),att(Z,X),not 1{defends_against(Y,X,Z):selected_arg(Y)}.

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
