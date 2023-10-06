# seqmod.py

def mod_sequence(seq, skip_index=None, truncate_index=None):
    """
    Rebuild the sequence based on provided skip and truncate indices.

    Parameters:
    seq: The input sequence.
    skip_index: Index to skip in the sequence. 
    truncate_index: Index to truncate the sequence from. 

    Return modified sequence.
    """

    seq_list = list(seq)  

    if truncate_index is not None and truncate_index < len(seq_list):
        seq_list = seq_list[:truncate_index]

    if skip_index is not None and skip_index < len(seq_list):
        seq_list.pop(skip_index)

    return seq_list
