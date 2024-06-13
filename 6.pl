bird(canary, true).
bird(ostrich, false).
bird(penguin, false).
bird(sparrow, true).
bird(eagle, true).

can_fly(Bird) :-
    bird(Bird, true),
    format('~w can fly.~n', [Bird]).

can_fly(Bird) :-
    bird(Bird, false),
    format('~w cannot fly.~n', [Bird]).
