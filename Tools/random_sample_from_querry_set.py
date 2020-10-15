
import random

def random_sample_from_querry_set(querry_set, n_sample):
    """
    Select a random sample from a querry set.

    Input:
        querry_set : django querry set from a model.
        n_sample : size of the sample
    Output:
        sample : django querry set
    """

    n_querry_set = len(querry_set)

    if n_querry_set < n_sample:
        print("Unable to do a random sample. Not enough data. Returning entire set")
        return querry_set
    else:
        shuffling = list(range(n_querry_set))
        random.shuffle(shuffling)
        shuffling = shuffling[:100]

        sample = [ querry_set[idx] for idx in shuffling ]

        return sample
