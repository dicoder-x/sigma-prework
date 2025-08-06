#https://www.codewars.com/kata/57ecf6efc7fe13eb070000e1
def outed(meet, boss):
    return 'Get Out Now!' if (sum(meet.values()) + meet[boss]) / len(meet) <= 5 else 'Nice Work Champ!'

#https://www.codewars.com/kata/57ed4cef7b45ef8774000014
score = {"accounts": 1, "finance": 2, "canteen": 10, "regulation": 3, "trading": 6, "change": 6, "IS": 8, "retail": 5, "cleaning": 4, "pissing about": 25}

def boredom(staff):
    total = sum(score[department] for department in staff.values())
    return 'kill me now' if total <= 80 else 'i can handle this' if total < 100 else 'party time!!'