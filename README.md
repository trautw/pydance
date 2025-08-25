```
(0,0)
    1M    1L
    (1,1) (1,2)

    2M    2L
    (2,1) (2,2)

    3M    3L
    (3,1) (3,2)

    4M    4L
    (4,1) (4,2)
```

```
(pydance) christophtrautwein@MacBook-Air-von-Christoph pydance % make
python main.py dance.yaml
Mairies Wedding
Complex Figure:
[{'complex_figure_name': 'first four bars', 'figure_list': [{'strang': 1, 'comment': '1C', 'list': [{'anchor': {'x': 0, 'y': 0}, 'figure_name': 'Turn Right'}, {'anchor': {'x': 0, 'y': 0}, 'figure_name': 'Cast'}]}, {'strang': 2, 'comment': '2M', 'list': [{'anchor': {'x': 1, 'y': 0}, 'figure_name': 'Stand'}, {'anchor': {'x': 1, 'y': 0}, 'figure_name': 'Stepup'}]}, {'strang': 3, 'comment': '2L', 'list': [{'anchor': {'x': 1, 'y': 1}, 'figure_name': 'Stand'}, {'anchor': {'x': 1, 'y': 1}, 'figure_name': 'Stepup'}]}]}]

== Complex figure: first four bars
Comment: 1C
Figure Name: Turn Right
Figure List Object: Turn Right, Anchor: {'x': 0, 'y': 0}
Figure Name: Cast
Figure List Object: Cast, Anchor: {'x': 0, 'y': 0}

Comment: 2M
Figure Name: Stand
Figure List Object: Stand, Anchor: {'x': 1, 'y': 0}
Figure Name: Stepup
Figure List Object: Stepup, Anchor: {'x': 1, 'y': 0}

Comment: 2L
Figure Name: Stand
Figure List Object: Stand, Anchor: {'x': 1, 'y': 1}
Figure Name: Stepup
Figure List Object: Stepup, Anchor: {'x': 1, 'y': 1}
```