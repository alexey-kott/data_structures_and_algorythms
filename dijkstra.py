

import pandas as pd


if __name__ == "__main__":
    adjacency_matrix = [
        [0, None, None, None, 10],
        [10, None, None, 40,  None],
        [30, None, None, 20, 10],
        [50, None, None, None, 30],
        [10, None, 10, None, None]
    ]

    df = pd.DataFrame(adjacency_matrix,
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['a', 'b', 'c', 'd', 'e']).T

    print(df)