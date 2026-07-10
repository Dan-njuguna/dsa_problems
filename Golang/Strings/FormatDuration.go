package kata

import (
	"fmt"
	"strings"
)

func FormatDuration(seconds int64) string {
	if seconds == 0  {
		return "now"
	}
	units := []struct{
		name	string
		value	int64
	}{
		{"year", 365 * 24 * 60 * 60},
		{"day", 24 * 60 * 60},
		{"hour", 60 * 60},
		{"minute", 60},
		{"second", 1},
	}

	var parts []string
	
	for _, unit := range units {
		if seconds >= unit.value {
			count := seconds / unit.value
			seconds %= unit.value

			if count == 1 {
				parts = append(parts, fmt.Sprintf("%d %s", count, unit.name))
			} else {
				parts = append(parts, fmt.Sprintf("%d %ss", count, unit.name))
			}
		}
	}

	switch len(parts) {
	case 1: 
		return parts[0]
	case 2:
		return parts[0] + " and " + parts[1]
	default:
		return strings.Join(parts[:len(parts)-1], ", ") + " and " + parts[len(parts)-1]
	}

}
