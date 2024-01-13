

% Generate
{selected_arg(X):arg(X)}:-.

% the reason we didn't just use ' not selected_arg(X)' is because we would get unsafe error
not_selected_arg(X):-arg(X),not selected_arg(X).

% Test for preferred
:- selected_arg(X),selected_arg(Y),att(X,Y).
defends_against(X,Y,Z):-arg(X),arg(Y),arg(Z),att(Z,Y),att(X,Z).
:-selected_arg(X),not_selected_arg(Z),att(Z,X),not 1{defends_against(Y,X,Z):selected_arg(Y)}.
%:-not_selected_arg(X),not att(X,X),not 1{att(X,Y):selected_arg(Y)},not 1{att(Y,X):selected_arg(Y)}.
preferred_condition(X):-not_selected_arg(X),not att(X,X),not 1{att(X,Y):selected_arg(Y)},not 1{att(Y,X):selected_arg(Y)}.

% Arguments
arg(1..4).
%arg(1).


% Attacks
att(1,2). 
att(1,4).  
att(2,1).
%att(1,1).


#minimize {X:preferred_condition(X)}.

#show selected_arg/1.
%#show not_selected_arg/1. 