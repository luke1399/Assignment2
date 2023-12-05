def check_dict_keys_are_correct(k1, k2):
    for split in k1:
        if split not in k2:
            return False
    return True
