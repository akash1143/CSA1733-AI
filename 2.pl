name_dob('Alice', date(1990, 5, 21)).
name_dob('Bob', date(1985, 3, 15)).
name_dob('Charlie', date(1992, 11, 30)).
name_dob('Diana', date(1988, 7, 19)).

find_dob(Name, DOB) :-
    name_dob(Name, DOB).

find_name(DOB, Name) :-
    name_dob(Name, DOB).
