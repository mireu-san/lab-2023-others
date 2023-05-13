# def solution(wallpaper):
#     x_axis = []
#     y_axis = []

#     for i in range(len(wallpaper)):
#         for j in range(len(wallpaper[i])):
#             if wallpaper[i][j] == "#":
#                 x_axis.append(i)
#                 y_axis.append(j)

#     lux = min(x_axis)
#     luy = min(y_axis)

#     rdx = max(x_axis)
#     rdy = max(y_axis)

#     if lux == rdx:
#         rdx += 1
#     if luy == rdy:
#         rdy += 1

#     return [lux, luy, rdx, rdy]
