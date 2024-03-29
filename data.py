p = [[[2, 3, 4, 4, 5],
      [2, 3, 3, 4, 4],
      [1, 2, 3, 4, 4],
      [1, 2, 2, 3, 3],
      [1, 1, 2, 2, 3]],
     [[2, 3, 4, 5, 5],
      [2, 3, 4, 4, 4],
      [1, 2, 3, 3, 4],
      [1, 2, 3, 3, 3],
      [1, 1, 2, 2, 3]],
     [[3, 3, 4, 5, 5],
      [2, 3, 4, 4, 5],
      [2, 2, 3, 4, 4],
      [1, 2, 3, 3, 4],
      [1, 2, 2, 3, 3]],
     [[3, 3, 4, 5, 5],
      [2, 3, 4, 4, 5],
      [2, 3, 3, 4, 5],
      [1, 2, 3, 4, 4],
      [1, 2, 3, 3, 4]]]
costs = [
    [92.6, 201.0, 274.2, 352.9, 425.0],
    [83.0, 149.7, 182.0, 249.3, 302.4],
    [56.2, 108.7, 158.6, 193.1, 241.6],
    [27.7, 58.4, 82.3, 99.4, 126.7],
]
calculations = [
    [
        [2, 4, 1, 249.30, 92.60, 341.90, 341.90],
        [2, 2, 2, 149.70, 201.00, 350.70, 341.90],
        [2, 1, 3, 83.00, 274.20, 357.20, 341.90],
        [3, 4, 2, 249.30, 201.00, 450.30, 450.30],
        [3, 3, 3, 182.00, 274.20, 456.20, 450.30],
        [3, 2, 4, 149.70, 352.90, 502.60, 450.30],
        [3, 1, 5, 83.00, 425.00, 508.00, 450.30],
        [4, 5, 3, 302.40, 274.20, 576.60, 534.90],
        [4, 3, 4, 182.00, 352.90, 534.90, 534.90],
        [5, 5, 5, 302.40, 425.00, 727.40, 727.40]
    ],
    [
        [3, 4, 2, 193.1, 341.9, 535.0, 535.0,],
        [3, 2, 3, 108.7, 450.3, 559.00, 559.00],
        [3, 1, 5, 56.2, 727.4, 783.60, 643.40],
        [4, 4, 3, 193.1, 450.3, 643.40, 643.40],
        [4, 3, 5, 158.6, 727.4, 886.00, 643.40],
        [5, 5, 4, 241.6, 534.9, 776.50, 776.50]
    ],
    [
        [1, 1, 1, 27.7, 83, 110.7, 110.7],
        [2, 3, 1, 82.3, 83, 165.3, 165.3],
        [2, 1, 2, 27.7, 149.7, 177.4, 165.3],
        [4, 4, 3, 99.4, 182, 281.4, 281.4],
        [4, 3, 4, 82.3, 249.3, 331.6, 281.4],
        [4, 2, 5, 58.4, 302.4, 360.8, 281.4]
    ],
    [
        [4, 4, 3, 281.4, 535, 816.4, 808.7],
        [4, 2, 4, 165.3, 643.4, 808.7, 808.7],
        [4, 1, 5, 110.7, 776.5, 887.2, 808.7]
    ]
]
count_calculation = [
    [
        [2, 4, 2, 1, 1, 1, 3],
        [2, 2, 2, 1, 1, 1, 3],
        [2, 1, 3, 1, 1, 1, 3],
        [3, 4, 2, 1, 1, 1, 4],
        [3, 3, 3, 1, 1, 1, 4],
        [3, 2, 4, 1, 1, 1, 4],
        [3, 1, 5, 1, 1, 1, 4],
        [4, 5, 3, 1, 1, 1, 2],
        [4, 3, 4, 1, 1, 1, 2],
        [5, 5, 5, 1, 1, 1, 1]
    ],
    [
        [3, 4, 2, 1, 3, 3, 3],
        [3, 2, 3, 1, 4, 4, 3],
        [3, 1, 5, 1, 1, 1, 3],
        [4, 4, 3, 1, 4, 4, 2],
        [4, 3, 5, 1, 1, 1, 2],
        [5, 5, 4, 1, 2, 2, 1]
    ],
    [
        [1, 1, 1, 1, 1, 1, 1],
        [2, 3, 1, 1, 1, 1, 2],
        [2, 1, 2, 1, 1, 1, 2],
        [4, 4, 3, 1, 1, 1, 3],
        [4, 3, 4, 1, 1, 1, 3],
        [4, 2, 5, 1, 1, 1, 3]
    ],
    [
        [4, 4, 3, 3, 3, 9, 3],
        [4, 2, 4, 2, 2, 4, 3],
        [4, 1, 5, 1, 1, 1, 3]
    ]
]
count_p = [
    [0, 3, 4, 2, 1, 10, 10],
    [0, 0, 3, 2, 1, 6, 60],
    [1, 2, 0, 3, 0, 6, 360],
    [0, 0, 0, 3, 0, 3, 1080],
]
cost_p = [
    [0, 341.9, 450.3, 534.9, 727.4],
    [0, 0, 535, 643.4, 776.5],
    [110.7, 165.3, 0, 281.4, 0],
    [0, 0, 0, 808.7, 0],
]

columns_for_calc = [("К2", "К1"), ("К3", "П1"), ("К4", "К2"), ("П3", "П2")]
