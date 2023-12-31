
% Generate
{selected_arg(X):arg(X)}:-.
% the reason we didn't just use ' not selected_arg(X)' is because we would get unsafe error
not_selected_arg(X):-arg(X),not selected_arg(X).

% Test for conflict-free
% That is we check if we can find a pair of arguments in the selected arguments that attack each other or an argument that attacks itself and 
%don't consider the sets of arguments that satisfy the body of this integrity constraint
:- selected_arg(X),selected_arg(Y),att(X,Y).

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
