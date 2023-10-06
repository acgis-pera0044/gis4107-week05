import seqmod  

def test_mod_sequence1():
    seq = ['A', 'B', 'C', 'D']
    skip_index=None
    truncate_index=None
    expection=['A', 'B', 'C', 'D']
    actual=seqmod.mod_sequence(seq, skip_index, truncate_index)
    assert expection==actual

def test_mod_sequence2():
    seq = ['A', 'B', 'C', 'D']
    skip_index=0
    truncate_index=None
    expection=['B', 'C', 'D']
    actual=seqmod.mod_sequence(seq, skip_index, truncate_index)
    assert expection==actual

def test_mod_sequence3():
    seq = ['A', 'B', 'C', 'D']
    skip_index=1
    truncate_index=None
    expection=['A', 'C', 'D']
    actual=seqmod.mod_sequence(seq, skip_index, truncate_index)
    assert expection==actual

def test_mod_sequence4():
    seq = ['A', 'B', 'C', 'D']
    skip_index=1
    truncate_index=2
    expection=['A']
    actual=seqmod.mod_sequence(seq, skip_index, truncate_index)
    assert expection==actual

def test_mod_sequence5():
    seq = ['A', 'B', 'C', 'D']
    skip_index=2
    truncate_index=2
    expection=['A', 'B']
    actual=seqmod.mod_sequence(seq, skip_index, truncate_index)
    assert expection==actual

def test_mod_sequence6():
    seq = ['A', 'B', 'C', 'D']
    skip_index=3
    truncate_index=2
    expection=['A', 'B']
    actual=seqmod.mod_sequence(seq, skip_index, truncate_index)
    assert expection==actual

def test_mod_sequence7():
    seq = ['A', 'B', 'C', 'D']
    skip_index=4
    truncate_index=None
    expection=['A', 'B', 'C', 'D']
    actual=seqmod.mod_sequence(seq, skip_index, truncate_index)
    assert expection==actual

def test_mod_sequence8():
    seq = ['A', 'B', 'C', 'D']
    skip_index=None
    truncate_index=4
    expection=['A', 'B', 'C', 'D']
    actual=seqmod.mod_sequence(seq, skip_index, truncate_index)
    assert expection==actual

def test_mod_sequence9():
    seq = ['A', 'B', 'C', 'D']
    skip_index=1
    truncate_index=4
    expection=['A', 'C', 'D']
    actual=seqmod.mod_sequence(seq, skip_index, truncate_index)
    assert expection==actual





