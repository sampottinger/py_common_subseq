import itertools


def number_common_subsequences(seq_1, seq_2):
    # Use length plus one to provide a row and column in the subsequence table,
    # a row / column not corresponding to an element. This provides
    # initialization values to the algorithm and handles the edge case of
    # calculating an element in the subsequence table when that element is
    # either in the first row of the table or is the first element of a row.
    # This also includes the empty string a substring.
    seq_1_len = len(seq_1)
    seq_2_len = len(seq_2)
    seq_1_len_plus_1 = seq_1_len + 1
    seq_2_len_plus_1 = seq_2_len + 1
    
    # Initialize a 2D array consisting of seq_1_len_plus_1 by seq_2_len_plus_1
    # values. All elements start with a value of 0.
    subseq_table = map(
        lambda x: [0] * seq_1_len_plus_1,
        range(0, seq_2_len_plus_1)
    )

    # Indicate the empty string as a substring
    for first_row_index in xrange(0, len(subseq_table[0])):
        subseq_table[0][first_row_index] = 1
    for first_col_index in xrange(0, len(subseq_table)):
        subseq_table[first_col_index][0] = 1

    # Enumerate pairs of all row indicies > 1 and column indicies > 1 in
    # ascending order.
    row_indicies = xrange(1, seq_1_len_plus_1)
    col_indicies = xrange(1, seq_2_len_plus_1)
    index_pairs = map(
        lambda x: zip(itertools.repeat(x, seq_2_len), col_indicies),
        row_indicies
    )

    index_pairs_flattened = list(itertools.chain.from_iterable(index_pairs))

    for (row, col) in index_pairs_flattened:
        if seq_1[row-1] == seq_2[col-1]:
            new_cell_value = 2 * subseq_table[row - 1][col - 1]
        else:
            new_cell_value = subseq_table[row - 1][col]
            new_cell_value += subseq_table[row][col-1]
            new_cell_value -= subseq_table[row-1][col-1]
        subseq_table[row][col] = new_cell_value

    return subseq_table[seq_1_len][seq_2_len]


def add_matched_element(element, target_collection):
    new_elements = map(lambda x: x + element, target_collection)
    return target_collection.union(new_elements)


def find_common_subsequences(seq_1, seq_2):
    # Use length plus one to provide a row and column in the subsequence table,
    # a row / column not corresponding to an element. This provides
    # initialization values to the algorithm and handles the edge case of
    # calculating an element in the subsequence table when that element is
    # either in the first row of the table or is the first element of a row.
    # This also includes the empty string a substring.
    seq_1_len = len(seq_1)
    seq_2_len = len(seq_2)
    seq_1_len_plus_1 = seq_1_len + 1
    seq_2_len_plus_1 = seq_2_len + 1
    
    # Initialize a 2D array consisting of seq_1_len_plus_1 by seq_2_len_plus_1
    # values. All elements start with a value of 0.
    subseq_table = map(
        lambda x: [set()] * seq_1_len_plus_1,
        range(0, seq_2_len_plus_1)
    )

    # Indicate the empty string as a substring
    for first_row_index in xrange(0, len(subseq_table[0])):
        subseq_table[0][first_row_index].add('')
    for first_col_index in xrange(0, len(subseq_table)):
        subseq_table[first_col_index][0].add('')

    # Enumerate pairs of all row indicies > 1 and column indicies > 1 in
    # ascending order.
    row_indicies = xrange(1, seq_1_len_plus_1)
    col_indicies = xrange(1, seq_2_len_plus_1)
    index_pairs = map(
        lambda x: zip(itertools.repeat(x, seq_2_len), col_indicies),
        row_indicies
    )

    index_pairs_flattened = list(itertools.chain.from_iterable(index_pairs))

    for (row, col) in index_pairs_flattened:
        if seq_1[row-1] == seq_2[col-1]:
            diagonal_cell_value = subseq_table[row - 1][col - 1]
            matched_element = seq_1[row-1]
            new_cell_value = add_matched_element(matched_element,
                diagonal_cell_value)
        else:
            above_set = subseq_table[row - 1][col]
            left_set = subseq_table[row][col-1]
            new_cell_value = above_set.union(left_set)
        subseq_table[row][col] = new_cell_value

    return subseq_table[seq_1_len][seq_2_len]
