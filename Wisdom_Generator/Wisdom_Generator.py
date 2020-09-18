# Randomly selecting entries from my philosophical database
def Wisdom_Generator(number_of_results=1):
    import pandas as pd
    import random
    import numpy as np
    pd.set_option('display.max_rows', None)
    Brain = pd.read_pickle('Brain.pkl')
    Brain = Brain.where(
        Brain['Parent'].str.contains("What|How|Who|When|Why|What|Causes|Effects|Point|Problems|Risks") \
        & ~Brain['Child'].str.contains(
            "with/to|Six Ws|What|How|Who|When|Why|What|Causes|Effects|Point|Types|Problems|Parts|Risks")).dropna()
    #print(Brain)
    for x in range(number_of_results):
        randy = random.randint(0, len(Brain))
        print(Brain['Parent'].iloc[randy] \
              + " : " + Brain['Child'].iloc[randy])

Wisdom_Generator(10)