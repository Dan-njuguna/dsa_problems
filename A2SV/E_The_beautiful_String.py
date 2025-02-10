import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        s = list(input[ptr])
        ptr += 1
        len_s = len(s)
        count = 0
        for j in range(len_s - 3):
            if (s[j] == '1' and s[j+1] == '1' and s[j+2] == '0' and s[j+3] == '0'):
                count += 1
        q = int(input[ptr])
        ptr += 1
        for __ in range(q):
            i = int(input[ptr])
            v = int(input[ptr+1])
            ptr += 2
            pos = i - 1  # convert to 0-based
            start_j = max(0, pos - 3)
            end_j = min(pos, len_s - 4)
            # Subtract previous contributions
            for j in range(start_j, end_j + 1):
                if j < 0 or j > len_s - 4:
                    continue
                if (s[j] == '1' and s[j+1] == '1' and s[j+2] == '0' and s[j+3] == '0'):
                    count -= 1
            # Update the character
            s[pos] = '1' if v == 1 else '0'
            # Add new contributions
            for j in range(start_j, end_j + 1):
                if j < 0 or j > len_s - 4:
                    continue
                if (s[j] == '1' and s[j+1] == '1' and s[j+2] == '0' and s[j+3] == '0'):
                    count += 1
            # Output the result
            print("YES" if count > 0 else "NO")

if __name__ == "__main__":
    main()