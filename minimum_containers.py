import sys
from collections import defaultdict


min_containers_map = defaultdict(list)


try:
    load = int(input('Enter load: '))
    containers_input = input('list of continers: ')
    containers =  [int(n) for n in containers_input.replace(' ','').split(',')]
except Exception as e:
    print('................invalid input...................!!')
    sys.exit()


def get_containers(containers, load, min_containers_map):
    # initially min_reqd_containers is set to max load.
    min_reqd_containers = [0]*load
    smallest_container = min(containers)
    if load in containers or load < smallest_container:
        selected_container = max([smallest_container, load])
        min_containers_map[load].append(selected_container)
        return [selected_container]
    elif min_containers_map.get(load):
        return min_containers_map[load]
    for i in [c for c in containers if c <= load ]:
        reqd_containers = [i]
        reqd_containers.extend(get_containers(containers, load-i, min_containers_map))
        if len(reqd_containers) < len(min_reqd_containers):
            min_reqd_containers = reqd_containers
            min_containers_map[load] = min_reqd_containers
    
    return min_reqd_containers

if __name__ == '__main__':
    min_reqd_containers = get_containers(containers, load, min_containers_map)
    print('................min_reqd_containers: ', min_reqd_containers)
