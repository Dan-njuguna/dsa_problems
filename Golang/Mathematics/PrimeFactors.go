package kata

import (
	"fmt"
	"sort"
)

func GetFactors(n int) []int {
	var factors []int

	for i := 2; i*i <= n; i++ {
		for n%i == 0 {
			factors = append(factors, i)
			n /= i
		}
	}

	// If anything remains, it is a prime factor.
	if n > 1 {
		factors = append(factors, n)
	}

	return factors
}

func PrimeFactors(n int) string {
	if n <= 1 {
		return ""
	}

	var result string

	factors := GetFactors(n)

	counts := make(map[int]int)

	for _, num := range factors {
		counts[num]++
	}
	keys := make([]int, 0, len(counts))
	for k := range counts {
		keys = append(keys, k)
	}

	sort.Ints(keys)

	for _, num := range keys {
		cnt := counts[num]
		if cnt > 1 {
			result += fmt.Sprintf("(%d**%d)", num, cnt)
		} else {
			result += fmt.Sprintf("(%d)", num)
		}
		delete(counts, cnt)  // Prevent Duplicate Counts
	}
	return result
}