def rotate_90_counterclockwise(metrics):
    return [list(row) for row in zip(*metrics) ][::-1]
metrics=[[1,2,3],
         [4,5,6],
         [7,8,9]]
z=rotate_90_counterclockwise(metrics)
for row in z:
    print(row)
    