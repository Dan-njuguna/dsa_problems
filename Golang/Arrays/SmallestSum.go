package kata

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func SmallestPossibleSum(ar []int) int {
	if len(ar) == 0 {
		return 0
	}

	g := ar[0]
	for i := 0; i < len(ar); i++ {
		g = gcd(g, ar[i])
	}

	return g * len(ar)
}