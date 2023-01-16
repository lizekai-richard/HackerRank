def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    r_max, r_min = n, 1
    c_max, c_min = n, 1
    dr_max, dr_min = r_q + c_q - 1 if r_q + c_q <= (n + 1) else n, \
                     1 if r_q + c_q <= (n + 1) else r_q + c_q - n
    dc_max, dc_min = n - (r_q - c_q) if r_q - c_q >= 0 else n, \
                     1 if r_q - c_q >= 0 else c_q - r_q + 1
    rn, cn, drn, dcn = 0, 0, 0, 0
    for o in obstacles:
        r_o, c_o = o[0], o[1]
        if r_o == r_q:
            if c_o > c_q:
                cn += 1
                c_max = min(c_o, c_max)
            else:
                cn += 1
                c_min = max(c_o, c_min)
        if c_o == c_q:
            if r_o > r_q:
                rn += 1
                r_max = min(r_o, r_max)
            else:
                rn += 1
                r_min = max(r_o, r_min)
        if r_o + c_o == r_q + c_q:
            if r_o > r_q:
                drn += 1
                dr_max = min(r_o, dr_max)
            else:
                drn += 1
                dr_min = max(r_o, dr_min)
        if r_o - c_o == r_q - c_q:
            if c_o > c_q:
                dcn += 1
                dc_max = min(c_o, dc_max)
            else:
                dcn += 1
                dc_min = max(c_o, dc_min)

    # if r_max == 0:
    #     r_max = n
    # if r_min == n + 1:
    #     r_min = 1
    # if c_max == 0:
    #     c_max = n
    # if c_min == n + 1:
    #     c_min = 1
    # if dr_max == 0:
    #     dr_max = r_q + c_q - 1 if r_q + c_q <= n else n
    # if dr_min == n + 1:
    #     dr_min = 1 if r_q + c_q <= n else r_q + c_q - n
    # if dc_max == 0:
    #     dc_max = n - (c_q - r_q) if c_q - r_q >= 0 else n
    # if dc_min == n + 1:
    #     dc_min = 1 if c_q - r_q >= 0 else r_q - c_q + 1

    num_of_attack = 0
    num_of_attack += (r_max - r_min - rn)
    num_of_attack += (c_max - c_min - cn)
    num_of_attack += (dr_max - dr_min - drn)
    num_of_attack += (dc_max - dc_min - dcn)

    return num_of_attack


if __name__ == '__main__':
    print(queensAttack(5, 3, 4, 3, [[2, 3], [5, 5], [4, 2]]))