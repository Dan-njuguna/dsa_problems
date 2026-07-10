package kata

import "strconv"

// ValidISBN10 - checks if a given string is valid ISBN number.
// An ISBN-10 number is valid if the sum of the digits multiplied
// by their position modulo 11 equals zero.
func ValidISBN10(isbn string) bool {
	if len(isbn) != 10 {
		return false
	}

	sum := 0

	for i, val := range isbn {
		var n int

		if val == 'X' || val == 'x' {
			if i != 9 {
				return false
			}
			n = 10
		} else {
			v, err := strconv.Atoi(string(val))
			if err != nil {
				return false
			}
			n = v
		}

		sum +=  n * (i + 1)
	}

	return sum % 11 == 0
}