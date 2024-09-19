from pyvis.network import Network

projects = {
    'Project_A': {
        'id': 'A',
        'name': 'project a',
        'outputs' : ['method_a', 'method_b', 'method_c'],
        'people': ['rse_1', 'rse_2', 'dev_1']
    },
    'Project_B': {
        'id': 'B',
        'name': 'project b',
        'outputs' : ['method_b', 'method_c'],
        'people' : ['rse_1', 'dev_1', 'dev_2']
    },
    'Project_C': {
        'id': 'C',
        'name': 'project c',
        'outputs' : ['method_c', 'method_e', 'method_f', 'method_g'],
        'people' : ['rse_3', 'dev_2', 'dev_3']
    },
    'Project_D': {
        'id': 'D',
        'name': 'project c',
        'outputs' : ['method_c', 'method_b', 'method_f', 'method_a'],
        'people' : ['rse_4', 'dev_1', 'dev_3']
    }
}

G = Network(notebook=False, height='1000px', width='100%')#, select_menu=True)

for project in projects:
    G.add_node(project, size=10, label=project, title=projects[project]['name'], group='projects', shape='ellipse')
    for output in projects[project]['outputs']:
        G.add_node(output, size=5, label=output, group='outputs', shape='ellipse')
        G.add_edge(project, output, weight=2, color='#009900')
    for person in projects[project]['people']:
        G.add_node(person, size=5, label=person, group='people', shape='ellipse')
        G.add_edge(project, person, weight=1, color='#990000')
G
#G.show_buttons(filter_=['groups'])
G.show('index.html', notebook=False)
