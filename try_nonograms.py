from nonogram import solve_nonogram, print_sol


HANUKIA = [
    [
        [1, 1, 1, 1, 2, 1, 1, 1, 1],
        [2], [1, 1, 1, 1, 2, 1, 1, 1, 1],
        [1, 1, 1, 6, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 1],
        [1, 1, 10, 1, 1],
        [1, 1, 2, 1, 1],
        [1, 14, 1],
        [1, 2, 1],
        [18],
        [2],
        [1, 2],
        [5, 2, 1],
        [3, 4, 5],
        [1, 6, 3],
        [8, 1]
    ],
    [
        [1, 8, 1],
        [1, 2],
        [1, 6, 1, 4],
        [1, 1, 2],
        [1, 4, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 2, 1, 1, 1, 2],
        [1, 1, 1, 1, 3],
        [16],
        [16],
        [1, 1, 1, 1, 3],
        [1, 2, 1, 1, 1, 2],
        [1, 1, 1, 1],
        [1, 4, 1, 1, 1],
        [1, 1, 2],
        [1, 6, 1, 4],
        [1, 2],
        [1, 8, 1]
    ]
]

PHONE = [
    [
        [11], [11, 2], [13,2], [18], [20], [6, 6], [5, 8, 5], [3, 3, 1, 4, 3],
        [2, 9], [5, 5], [2, 2, 2, 5], [5, 4, 5], [2, 2, 6, 5], [5, 6, 5],
        [3, 2, 4, 6], [7, 2, 7], [4, 3, 3, 4], [6, 9, 3], [7, 1, 8], [16]
    ],
    [
     [3, 4], [5, 8], [6, 10], [7, 3, 1, 5], [6, 2, 5, 3], [6, 13],
     [5, 2, 2, 2, 2], [5, 4, 2, 4], [5, 1, 1, 4, 1, 1], [5, 3, 6, 3],
     [5, 1, 1, 6, 1, 1], [5, 3, 4, 3], [5, 4, 2, 4], [5, 5, 5], [1, 4, 13],
     [2, 4, 8, 3], [7, 8, 2], [6, 10], [5, 8], [3, 4]
    ]
]

NONOGRAM_3 = [
               [[4, 4],[4, 4],[4, 4],[1, 4, 2, 4, 2],[2, 8, 8],[3, 10, 10],
                [7, 7],[7, 7],[7, 7],[3, 2, 3, 2],[3, 3],[1, 1],[4, 4],
                [4, 4],[4, 4],[1, 4, 2, 4, 2],[2, 8, 8],[3, 10, 10],
                [7, 7],[7, 7],[7, 7],[3, 2, 3, 2],[3, 3],[1, 1],[4, 4],
                [4, 4],[4, 4],[1, 4, 2, 4, 2],[2, 8, 8],[3, 10, 10]],
            [[3, 1, 3, 1, 3], [2, 4, 2, 4, 2], [1, 1, 4, 1, 1, 4, 1, 1],
             [2, 4, 2, 4, 2], [4, 4, 4, 4, 4, 1], [9, 9, 6], [9, 9, 5],
             [8, 8, 4], [4, 4, 2], [3, 3, 2], [3, 3, 3], [3, 1, 3, 1, 3],
             [2, 4, 2, 4, 2], [1, 1, 4, 1, 1, 4, 1, 1], [2, 4, 2, 4, 2],
             [4, 4, 4, 4, 4, 1], [9, 9, 6], [9, 9, 5], [8, 8, 4], [4, 4, 2],
             [3, 3, 2], [3, 3, 3], [3, 3, 3], [2, 2, 2], [1, 1, 1]
             ]
]


blocks_1 = [
            [
                [7],[7],[1,1,1,1],[3,3],[3,3],[2,1,1,2],[3,3],[9],[7],[2,2],
                [2,3], [6,1],[2,2,3],[4,3,1],[2,3,1,3],[3,1,5],[4,5],[4,5],
                [1,1,1,1],[1,1,1,1]
            ],
            #cols
            [
                [4],[7],[3,2,3],[4,1,4,4],[2,2,3,2,3],[3,8,1],[2,4,2],[2,2,2],
                [2,6,1],[3,6,3], [2,2,3,3,3],[4,1,1,6],[3,5],[6],[3]
            ]
]


tower_X2 = [
            [
            [1,8], [3,11], [1,14], [5,17], [7,15], [1,1,1,1,9], [1,1,1,1,3],
                [9], [1,1,1,1,4], [1,1,1,1,12], [8,17], [6,14], [1,7,1,12],
                [11,9], [9,7], [9,4], [8,2], [7], [7], [1,5], [1,5], [1,7,1],
                [11], [6,3], [5,2], [4,1],[7], [7], [1,5], [1,5], [1,5], [7,2],
                [4,1,2], [5,13], [5,14], [22], [2,19], [2,20],[23], [11,2,1,3],
                [11,2,1,2], [23], [28], [30], [30],[1,8], [3,11], [1,14],
                [5,17], [7,15], [1,1,1,1,9], [1,1,1,1,3], [9], [1,1,1,1,4],
                [1,1,1,1,12], [8,17], [6,14], [1,7,1,12], [11,9], [9,7], [9,4],
                [8,2], [7], [7], [1,5], [1,5], [1,7,1], [11], [6,3], [5,2],
                [4,1], [7], [7], [1,5], [1,5], [1,5], [7,2], [4,1,2], [5,13],
                [5,14], [22], [2,19], [2,20],[23], [11,2,1,3], [11,2,1,2],
                [23], [28], [30], [30]
            ],
            #cols
            [
                [2], [3], [2,3,3], [4,3,3,12], [4,1,33],[2,1,9,7,5,7], [1,42],
                [5,1,35], [1,20,6,10], [2,1,13,6,10], [4,35], [3,4,3,12],
                [2,2,3,12], [4,3,12], [4,3,8,4], [4,3,8,4], [4,4,12], [4,3,12],
                [4,4,6,4], [5,4,6,4],[5,4,12], [4,5,6,4], [5,5,6,4],[5,6,11],
                [5,6,10], [5,5,3,4], [5,6,3], [4,6,3], [4,7,3], [4,7,3],[2],
                [3], [2,3,3], [4,3,3,12], [4,1,33],[2,1,9,7,5,7], [1,42],
                [5,1,35], [1,20,6,10], [2,1,13,6,10], [4,35], [3,4,3,12],
                [2,2,3,12], [4,3,12], [4,3,8,4], [4,3,8,4], [4,4,12], [4,3,12],
                [4,4,6,4], [5,4,6,4],[5,4,12], [4,5,6,4], [5,5,6,4],[5,6,11],
                [5,6,10], [5,5,3,4], [5,6,3], [4,6,3], [4,7,3], [4,7,3]
            ]
]


print_sol(solve_nonogram(HANUKIA))
print_sol(solve_nonogram(PHONE))
print_sol(solve_nonogram(NONOGRAM_3))
print_sol(solve_nonogram(blocks_1))
