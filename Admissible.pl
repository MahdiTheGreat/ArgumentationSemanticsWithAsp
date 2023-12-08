% Generate
{selected_arg(X):arg(X)}:-.
% the reason we didn't just use ' not selected_arg(X)' is because we would get unsafe error
not_selected_arg(X):-arg(X),not selected_arg(X).

% Test for admissible
%Notice that we use the same line we used in the Conflict-free program and that is because a stable set has to be at first conflict-free. 
% we also check if there is an unselected argument that isn't attacked by at least one of our selected arguments. 
% With this program we find sets of arguments that attack all the unselected arguments and in a way this extension is more conservative 
% and follows the idea of "You are either with us, or against us".
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
