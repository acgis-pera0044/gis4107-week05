def mod_sequence(seq, skip_index = None, truncate_index = None):
    position_index = 0
    final_result = ""
    for element in seq:
        if position_index == skip_index: 
            if position_index == truncate_index:
                break
            position_index += 1
            continue
        if position_index == truncate_index: break
        position_index += 1
        final_result += str(element)
    return final_result