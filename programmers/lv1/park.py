# 172928
def solution(park, routes):
    # First, find the starting position of the robot dog in the park.
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                x, y = i, j

    # Define the information about the direction in advance.
    dx = {"N": -1, "S": 1, "E": 0, "W": 0}
    dy = {"N": 0, "S": 0, "E": 1, "W": -1}

    # Execute the loop for each route.
    for route in routes:
        direction, distance = route.split()
        distance = int(distance)

        # Calculate the position where the robot dog moved the maximum distance in the given direction.
        nx, ny = x + dx[direction] * distance, y + dy[direction] * distance

        # If the calculated position is out of range of the park or there is an obstacle, it does not move.
        if (
            nx < 0
            or ny < 0
            or nx >= len(park)
            or ny >= len(park[0])
            or "X" in park[min(x, nx) : max(x, nx) + 1][min(y, ny) : max(y, ny) + 1]
        ):
            continue

        # Otherwise, update the position.
        x, y = nx, ny

    # Return the position of the robot dog after performing all commands.
    return [x, y]
