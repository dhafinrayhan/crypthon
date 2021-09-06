import tools


def vigenere(P: str, K: str, decrypt=False) -> str:
    P = tools.filter_alpha(P).upper()
    K = tools.filter_alpha(K).upper()
    C = ''
    m = len(K)

    P_ascii = tools.str_to_ascii_list(P)
    K_ascii = tools.str_to_ascii_list(K)

    mode = -1 if decrypt else 1

    for i in range(len(P)):
        p_ix = P_ascii[i] - 65
        k_ix = K_ascii[i % m] - 65
        c_ix = (p_ix + mode * k_ix) % 26

        C += chr(65 + c_ix)

    return C


def auto_key_vigenere(P: str, K: str, decrypt=False) -> str:
    P = tools.filter_alpha(P).upper()
    K = tools.filter_alpha(K).upper()
    C = ''

    P_ascii = tools.str_to_ascii_list(P)
    K_ascii = tools.str_to_ascii_list(K)

    mode = -1 if decrypt else 1

    for i in range(len(P)):
        p_ix = P_ascii[i] - 65
        k_ix = K_ascii[i] - 65
        c_ix = (p_ix + mode * k_ix) % 26

        K_ascii.append(65 + (c_ix if decrypt else p_ix))

        C += chr(65 + c_ix)

    return C


def extended_vigenere(P: str, K: str, decrypt=False) -> str:
    C = ''
    m = len(K)

    P_ascii = tools.str_to_ascii_list(P)
    K_ascii = tools.str_to_ascii_list(K)

    mode = -1 if decrypt else 1

    for i in range(len(P)):
        p_ix = P_ascii[i]
        k_ix = K_ascii[i % m]
        c_ix = (p_ix + mode * k_ix) % 256

        C += chr(c_ix)

    return C


def playfair(P: str, K: str, decrypt=False) -> str:
    def clean_key(s: str) -> str:
        l = []

        for c in s:
            if c not in l and c != 'J':
                l.append(c)

        return ''.join(l)

    def index_to_pos(ix: int) -> tuple:
        return (ix // 5, ix % 5)

    def pos_to_index(pos: tuple) -> int:
        row, col = pos
        return 5 * row + col

    def shift_right(ix: int, step=1) -> int:
        row, col = index_to_pos(ix)
        col = (col + step) % 5
        return pos_to_index((row, col))

    def shift_down(ix: int, step=1) -> int:
        row, col = index_to_pos(ix)
        row = (row + step) % 5
        return pos_to_index((row, col))

    def same_row(ix1: int, ix2: int) -> bool:
        row1, col1 = index_to_pos(ix1)
        row2, col2 = index_to_pos(ix2)
        return row1 == row2

    def same_col(ix1: int, ix2: int) -> bool:
        row1, col1 = index_to_pos(ix1)
        row2, col2 = index_to_pos(ix2)
        return col1 == col2

    P = tools.filter_alpha(P).upper().replace('J', 'I')
    K = clean_key(tools.filter_alpha(K).upper())

    K_square = K
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    for a in alphabet:
        if a not in K_square:
            K_square += a

    P_len = len(P)
    P_bigram = []

    i = 0
    while i < P_len:
        if (i == P_len - 1) or (P[i] == P[i+1]):
            P_bigram.append(P[i] + 'X')
            i += 1
        else:
            P_bigram.append(P[i:i+2])
            i += 2
    
    C = ''
    mode = -1 if decrypt else 1

    for i in range(len(P_bigram)):
        a = P_bigram[i][0]
        b = P_bigram[i][1]

        a_ix = K_square.index(a)
        b_ix = K_square.index(b)

        a_row, a_col = index_to_pos(a_ix)
        b_row, b_col = index_to_pos(b_ix)

        if same_row(a_ix, b_ix):
            v_ix = shift_right(a_ix, mode)
            w_ix = shift_right(b_ix, mode)
        elif same_col(a_ix, b_ix):
            v_ix = shift_down(a_ix, mode)
            w_ix = shift_down(b_ix, mode)
        else:
            v_ix = pos_to_index((a_row, b_col))
            w_ix = pos_to_index((b_row, a_col))

        v = K_square[v_ix]
        w = K_square[w_ix]

        C += v + w

    return C
