def is_merge(s, part1, part2):
    ind_p = []
    for part in [part1,part2]:
        for i,p in enumerate(part):
            if p in s:
                ind_p.append(p)
    return len(ind_p) == len(s)
is_merge('codewars', 'cod', 'wars')