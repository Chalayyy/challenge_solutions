"""
The problem: 
Given a list of entrances, a list of exits (which are
disjoint from the entrances), and a matrix indicating the maximum
number of individuals that can travel down a hallway each time unit
from one room(the matrix row) to another (the matrix column), find the
maximum number of individuals that can be sent from the entrances to
the exits.

The solution:
 To solve this, start from the exits and note how many
individuals each room receives and how many it sends to already-visited
rooms (assuming entrances can receive an infinite amount and exits can
send an infinite amount. Move to all the rooms that sent to the last
set of rooms and see how many it sends/ receives. If a room ever sends
more than it receives, then starting at previous set of rooms it sent
to, find if any rooms receive more than it sends. Reduce how many
individuals a room receives if it can't send them all first by reducing
from the room that sent too many (if the two rooms are directly
connected). Repeat until no rooms so far visited take more than they
send. If this doesn't sufficiently reduce how many the over-sending
room sends, then reduce how many it sends, first to rooms which haven't
been visited(and therefore may or may not lead to the end), then to
rooms which have been visited (which now have been reduced to only
receive what they can send).

All rooms from the end up to this point now receive at least as many as
they send. Proceed to move back to rooms which send to the current set
and repeat the process. 

"""


def solution(entrances, exits, path):

    # change useless pathways to 0. These are pathways leading to the room it came
    # from, back to the original entrance, from the exits, or from rooms that
    # don't receive bunnies.
    for x in range(len(path)):
        path[x][x] = 0
        for y in entrances:
            path[x][y] = 0
        for z in exits:
            path[z][x] = 0
        if sum([path[y][x]] == 0 for y in range(len(path))):
            for y in range(len(path)):
                path[x][y] = 0

    # if a spot sends more than it recieves, reduce how much it sends to match how much it receives
    # start at end, work backwards
    # repeat until no more changes
    at = exits[:]  # start at ending
    coming_from = [x for x in range(len(path)) if any(
        path[x][y] != 0 for y in at)]  # rooms that send to "at"

    all_coming_from = []  # keep track of sets of rooms for backtracking
    all_coming_from.append(at)

    visited = []  # keep track of what spots are confirmed leading to the end
    visited.extend(at)

    # repeat until reached beginning
    while set(at) and not all(entrance in set(at) for entrance in entrances):

        all_coming_from.append(coming_from)

        each_receives = [sum(path[x][y] for x in range(len(path)))
                         for y in at]  # sum of column for each value in "at"
        each_sends = [sum(path[x][y] for y in visited)
                      for x in at]  # sum of row for each value in "at"
        # adjust entrance receives / exit sends values to match how much they send/receive respectively, rather than infinite.
        for spot in at:
            if spot in entrances:
                each_receives[at.index(spot)] = each_sends[at.index(spot)]
            if spot in exits:
                each_sends[at.index(spot)] = each_receives[at.index(spot)]

        # as long as any current spot sends more than it receives, reduce how much it sends to match how much it gets.
        while any([each_sends[x] > each_receives[x] for x in range(len(at))]):

            # check each room one at a time
            for k in range(len(at)):
                while each_sends[k] > each_receives[k]:

                    # if a spot is sending more than it gets, see which future spots are receiving more than they send and reduce how many they receive
                    index = -1
                    # start at set of rooms that the over-sending room sends to
                    start = all_coming_from[index-1]

                    # continue until we would try to start at the exits
                    while set(start) != set(exits):
                        # ignore entrances since no room sends to entrances
                        going_to = [
                            spot for spot in all_coming_from[index-2] if spot not in entrances]
                        going_receives = [
                            sum(path[x][y] for x in range(len(path))) for y in going_to]
                        going_sends = [sum(path[x][y]
                                           for y in visited) for x in going_to]
                        for x in going_to:
                            if x in exits:
                                going_sends[going_to.index(
                                    x)] = going_receives[going_to.index(x)]

                        # if any spot gets more than it sends, reduce how much it gets (does not affect its output)
                        while any([going_receives[x] > going_sends[x] for x in range(len(going_to))]):
                            for j in range(len(going_to)):

                                # reduce how much it gets from direct sources that are sending too much
                                if going_receives[j] > going_sends[j]:
                                    # if the one getting too much is getting from the one sending more than it receives, reduce how much is sent
                                    if path[at[k]][going_to[j]] > 0:
                                        path[at[k]][going_to[j]] -= min(
                                            going_receives[j] - going_sends[j], path[at[k]][going_to[j]])

                        # continue moving forward towards exit to find any other rooms that get too much
                        start = going_to[:]
                        index -= 1

                    # recalculate how much each room receives and sends
                    # sum of column for each value in "at"
                    each_receives = [sum(path[x][y]
                                         for x in range(len(path))) for y in at]
                    each_sends = [sum(path[x][y] for y in visited)
                                  for x in at]  # sum of row for each value in "at"
                    # adjust entrance receives / exit sends values to match how much they send/receive respectively, rather than infinite.
                    for spot in at:
                        if spot in entrances:
                            each_receives[at.index(
                                spot)] = each_sends[at.index(spot)]
                        if spot in exits:
                            each_sends[at.index(
                                spot)] = each_receives[at.index(spot)]

                    # if a spot still sends more than it gets, reduce how much it sends, first to non-visited spots
                    if each_sends[k] > each_receives[k]:
                        smallest = float("inf")
                        y_index = 0
                        for y in range(len(path)):
                            if y not in visited:  # check non-visited spots first
                                if path[at[k]][y] < smallest and path[at[k]][y] > 0:
                                    smallest = path[at[k]][y]
                                    y_index = y

                        # if room doesn't send to non-visited spots, reduce how many are sent to visited spots
                        if smallest == float("inf"):
                            for y in visited:
                                if path[at[k]][y] < smallest and path[at[k]][y] > 0:
                                    smallest = path[at[k]][y]
                                    y_index = y

                        # don't reduce more than the value itself
                        reduction = min(
                            path[at[k]][y_index], (each_sends[k] - each_receives[k]))
                        path[at[k]][y_index] -= reduction

                        # recalculate how much each room receives and sends
                        # sum of column for each value in "at"
                        each_receives = [sum(path[x][y]
                                             for x in range(len(path))) for y in at]
                        # sum of row for each value in "at"
                        each_sends = [sum(path[x][y]
                                          for y in visited) for x in at]
                        # adjust entrance receives / exit sends values to match how much they send/receive respectively, rather than infinite.
                        for spot in at:
                            if spot in entrances:
                                each_receives[at.index(
                                    spot)] = each_sends[at.index(spot)]
                            if spot in exits:
                                each_sends[at.index(
                                    spot)] = each_receives[at.index(spot)]

        # next step back to rooms that send to current set of rooms
        visited.extend(at)
        visited = list(set(visited))
        # recalculate coming_from for any changes
        coming_from = [x for x in range(len(path)) if any(
            path[x][y] != 0 for y in at)]
        at = coming_from[:]
        # recalculate coming_from based on new at
        coming_from = [x for x in range(len(path)) if any(
            path[x][y] != 0 for y in at)]

    # return sum of values sent directly to exit rooms since these are confirmed bunnies
    return sum(path[x][y] for x in range(len(path)) for y in exits)


# Example case:
print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [
      0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
