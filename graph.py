from pyvis.network import Network

projects = {
    'FDRI': {
        'id': 'xjxjsjh-1001-2020',
        'name': 'FDRI',
        'outputs' : ['pipelines', 'data lakes'],
        'people': ['Robin', 'Faiza', 'Joe']
    },
    'boost': {
        'id': 'xjsjsjcjc-1002-2024',
        'name': 'Research Data Cloud',
        'outputs' : ['pipelines', 'building blocks'],
        'people' : ['Robin', 'Faiza', 'Dominic']
    }
}

G = Network(notebook=False, select_menu=True)

for project in projects:
    G.add_node(project, size=10, label=project, title=projects[project]['name'], group='projects')
    for output in projects[project]['outputs']:
        G.add_node(output, size=5, label=output, group='outputs')
        G.add_edge(project, output, weight=2, color='#009900')
    for person in projects[project]['people']:
        G.add_node(person, size=5, label=person, group='people')
        G.add_edge(project, person, weight=1, color='#990000')
G.show_buttons(filter_=['groups'])
G.show('dri.html', notebook=False)
