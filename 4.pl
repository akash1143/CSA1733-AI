planet('Mercury', 57.9, 4.88).
planet('Venus', 108.2, 12.1).
planet('Earth', 149.6, 12.7).
planet('Mars', 227.9, 6.78).
planet_properties(Planet, Distance, Diameter) :-
    planet(Planet, Distance, Diameter).