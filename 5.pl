hanoi(1, From, To, _) :-
    format('Move top disk from ~w to ~w~n', [From, To]).
hanoi(N, From, To, Via) :-
    N > 1,
    N1 is N - 1,
    hanoi(N1, From, Via, To),
    hanoi(1, From, To, _),
    hanoi(N1, Via, To, From).
