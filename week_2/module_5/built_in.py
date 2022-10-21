actors = [
        { "name" : "sakib", "age" : 35},
        { "name" : "akib", "age" : 28},
        { "name" : "nakib", "age" : 38},
        { "name" : "asif", "age" : 25},
        { "name" : "nobel", "age" : 48}
    ]

sorted_actors = sorted(actors, key= lambda actor : actor["age"])
print(sorted_actors)
