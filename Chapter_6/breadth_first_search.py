from collections import deque
def is_person_seller(name):
    return name[-1] == 'm'

def breadth_first_search(graph):
    search_queue = deque()
    search_queue += graph['you']
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if is_person_seller(person):
                print(f'{person} is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

breadth_first_search(graph)