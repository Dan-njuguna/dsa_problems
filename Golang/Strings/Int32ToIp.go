package kata

import (
	"strings"
	"strconv"
)

func ConvertToBinary(n uint32) string {
	if n == 0 {
		return "0"
	}

	var bin []string

	for n > 0 {
		rem := n % 2
		if rem == 1 {
			bin = append(bin, "1")
		} else {
			bin = append(bin, "0")
		}
		n /= 2
	}

	for i, j := 0, len(bin)-1; i < j; i, j = i+1, j-1 {
		bin[i], bin[j] = bin[j], bin[i]
	}

	return strings.Join(bin, "")
}

func ConvertToInt32(bin string) uint32{
	var result uint32

	for _, bit := range bin {
		result <<= 1

		if bit == '1' {
			result |= 1
		}
	}

	return result
}

func ChunkString(s string, size int) []string {
	var chunks []string

	for i := 0; i < len(s); i += size {
		end := i + size
		if end > len(s) {
			end = len(s)
		}
		chunks = append(chunks, s[i:end])
	}

	return chunks
}

func Int32ToIP(num uint32) string {
	base2 := ConvertToBinary(num)

	chunks := ChunkString(base2, 8)

	var octets []string

	for _, chunk := range chunks {
		octet := ConvertToInt32(chunk)
		s := strconv.FormatUint(uint64(octet), 10)
		octets = append(octets, s)
	}

	return strings.Join(octets, ".")
}
