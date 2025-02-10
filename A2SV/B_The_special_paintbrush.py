#!/usr/bin/python3

def specialPaintbrush(s: str) -> int:
    special = [i for i, ch in enumerate(s) if ch == "B"]
    
    if not special:
        return 0  # No 'B' characters found

    return (max(special) - min(special)) + 1

# Use case
if __name__ == "__main__":
    n = int(input().strip())
    
    while n > 0:
        l = int(input().strip())
        s = input().strip().upper()
        
        if len(s) != l:
            exit()
        
        print(specialPaintbrush(s))
        n -= 1  # Decrement loop counter