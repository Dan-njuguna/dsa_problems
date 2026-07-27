package kata

import (
	"fmt"
	"strings"
)

func Solution(list []int) string {
	if len(list) == 0 {
		return ""
	}

	var parts []string

	for i := 0; i < len(list); { // Sample list of 3 elements.
		// Find the end of the consecutive sequence.
		j := i
		for j+1 < len(list) && list[j+1] == list[j]+1 {
			j++
		}

		runLength := j - i + 1

		switch {
		case runLength >= 3:
			// Compress into a range.
			parts = append(parts, fmt.Sprintf("%d-%d", list[i], list[j]))
		case runLength == 2:
			// Two numbers stay separate.
			parts = append(parts,
				fmt.Sprintf("%d", list[i]),
				fmt.Sprintf("%d", list[j]),
			)
		default:
			// Single number.
			parts = append(parts, fmt.Sprintf("%d", list[i]))
		}

		// Skip over the processed sequence.
		i = j + 1
	}

	return strings.Join(parts, ",")
}
