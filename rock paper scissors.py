def scorer(s: str) -> str:
    return {"RR": "=", "RP": "-", "RS":"+", "PR":"+", "PP": "=", "PS":"-", "SR":"-", "SP":"+", "SS":"="}[s]

def game_score(gam_string: str)->[str]:
    games = [g.strip() for g in game_string.split(",")]
    scores = [scorer(g) for g in games]
    return "+%d, -%d, =%d" %(scores.count("+"), scores.count("-"), scores.count("="))

game_string = "RP, RR, SP, SR"
print(game_score(game_string))
