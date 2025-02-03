test_cases = int(input())

lst = []
for i in range(test_cases):
    try:
        num = int(input())
        lst.append(num)
    except EOFError:
        break

# Divisions
"""
For Division 1: 1900≤rating
For Division 2: 1600≤rating≤1899
For Division 3: 1400≤rating≤1599
For Division 4: rating≤1399
"""

for i in range(test_cases):
    rating = lst[i]
    if rating >= 1900:
        print("Division 1")
    
    elif 1600 <= rating <= 1899:
        print("Division 2")
    elif 1400 <= rating  <= 1599:
        print("Division 3")
    else:
        print("Division 4")