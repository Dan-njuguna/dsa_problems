package kata

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}


// Manacher's Algorithm
func LongestPalindrome(s string) string {
	if len(s) <= 1 {
		return s
	}

	t := make([]rune, 0, 2*len(s)+3)
	t = append(t, '^')

	for _, ch := range s {
		t = append(t, '#', ch)
	}

	t = append(t, '#', '$')

	n := len(t)

	p := make([]int, n)

	center, right := 0, 0

	maxLen, centerIndex := 0, 0

	for i := 1; i < n-1; i++ {
		mirror := 2 * center - i

		if i < right {
			if p[mirror] < right-i {
				p[i] = min(right-1, p[mirror])
			}
		}

		for t[i+1+p[i]] == t[i-1-p[i]] {
			p[i]++
		}

		if p[i] > maxLen {
			maxLen = p[i]
			centerIndex = i
		}
	}

	start := (centerIndex - maxLen) / 2

	return s[start:start+maxLen]
}