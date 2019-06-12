def pick(n: int) -> int:
    return int(n % 5 == 0) + 2 * int(n % 7 == 0)

def alphabeta(n: int) -> str:
    return [str(n), "ALPHA", "BETA", "ALPHABETA"][pick(n)]

def gen_seq(n: int) -> [str]:
    return [alphabeta(i) for i in range(1, n)]

print(gen_seq(36))
