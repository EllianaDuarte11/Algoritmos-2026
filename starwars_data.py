# Datos de Star Wars para el grafo.
# Episodios (I a IX) en los que aparece cada personaje; de ahí salen los pesos de las aristas:
#   peso de la arista = cantidad de episodios en los que aparecieron juntos los dos personajes
#   Luke Skywalker  3, 4, 5, 6, 7, 8, 9
#   Darth Vader     3, 4, 5, 6
#   Yoda            1, 2, 3, 5, 6, 8
#   Boba Fett       2, 5, 6
#   C-3PO           1, 2, 3, 4, 5, 6, 7, 8, 9
#   Leia            3, 4, 5, 6, 7, 8, 9
#   Rey             7, 8, 9
#   Kylo Ren        7, 8, 9
#   Chewbacca       3, 4, 5, 6, 7, 8, 9
#   Han Solo        4, 5, 6, 7, 9
#   R2-D2           1, 2, 3, 4, 5, 6, 7, 8, 9
#   BB-8            7, 8, 9

personajes = [
    'Luke Skywalker',
    'Darth Vader',
    'Yoda',
    'Boba Fett',
    'C-3PO',
    'Leia',
    'Rey',
    'Kylo Ren',
    'Chewbacca',
    'Han Solo',
    'R2-D2',
    'BB-8',
]

# (personaje 1, personaje 2, episodios en común)
relaciones = [
    ('Luke Skywalker', 'Darth Vader', 4),
    ('Luke Skywalker', 'Yoda', 4),
    ('Luke Skywalker', 'Boba Fett', 2),
    ('Luke Skywalker', 'C-3PO', 7),
    ('Luke Skywalker', 'Leia', 7),
    ('Luke Skywalker', 'Rey', 3),
    ('Luke Skywalker', 'Kylo Ren', 3),
    ('Luke Skywalker', 'Chewbacca', 7),
    ('Luke Skywalker', 'Han Solo', 5),
    ('Luke Skywalker', 'R2-D2', 7),
    ('Luke Skywalker', 'BB-8', 3),
    ('Darth Vader', 'Yoda', 3),
    ('Darth Vader', 'Boba Fett', 2),
    ('Darth Vader', 'C-3PO', 4),
    ('Darth Vader', 'Leia', 4),
    ('Darth Vader', 'Chewbacca', 4),
    ('Darth Vader', 'Han Solo', 3),
    ('Darth Vader', 'R2-D2', 4),
    ('Yoda', 'Boba Fett', 3),
    ('Yoda', 'C-3PO', 6),
    ('Yoda', 'Leia', 4),
    ('Yoda', 'Rey', 1),
    ('Yoda', 'Kylo Ren', 1),
    ('Yoda', 'Chewbacca', 4),
    ('Yoda', 'Han Solo', 2),
    ('Yoda', 'R2-D2', 6),
    ('Yoda', 'BB-8', 1),
    ('Boba Fett', 'C-3PO', 3),
    ('Boba Fett', 'Leia', 2),
    ('Boba Fett', 'Chewbacca', 2),
    ('Boba Fett', 'Han Solo', 2),
    ('Boba Fett', 'R2-D2', 3),
    ('C-3PO', 'Leia', 7),
    ('C-3PO', 'Rey', 3),
    ('C-3PO', 'Kylo Ren', 3),
    ('C-3PO', 'Chewbacca', 7),
    ('C-3PO', 'Han Solo', 5),
    ('C-3PO', 'R2-D2', 9),
    ('C-3PO', 'BB-8', 3),
    ('Leia', 'Rey', 3),
    ('Leia', 'Kylo Ren', 3),
    ('Leia', 'Chewbacca', 7),
    ('Leia', 'Han Solo', 5),
    ('Leia', 'R2-D2', 7),
    ('Leia', 'BB-8', 3),
    ('Rey', 'Kylo Ren', 3),
    ('Rey', 'Chewbacca', 3),
    ('Rey', 'Han Solo', 2),
    ('Rey', 'R2-D2', 3),
    ('Rey', 'BB-8', 3),
    ('Kylo Ren', 'Chewbacca', 3),
    ('Kylo Ren', 'Han Solo', 2),
    ('Kylo Ren', 'R2-D2', 3),
    ('Kylo Ren', 'BB-8', 3),
    ('Chewbacca', 'Han Solo', 5),
    ('Chewbacca', 'R2-D2', 7),
    ('Chewbacca', 'BB-8', 3),
    ('Han Solo', 'R2-D2', 5),
    ('Han Solo', 'BB-8', 2),
    ('R2-D2', 'BB-8', 3),
]
