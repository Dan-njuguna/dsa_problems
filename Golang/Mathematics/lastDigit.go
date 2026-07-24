package kata

// phi - computes Euler's totient, which reduces enormous exponents.
func phi(n int) int {
	res := n
	x := n
	for p := 2; p*p <= x; p++ {
		if x%p == 0 {
			for x%p == 0 {
				x /= p
			}
			res -= res / p
		}
	}
	if x > 1 {
		res -= res / x
	}
	return res
}

// powMod - computes `a ^ b mod m` efficiently in O(log b).
func powMod(a, b, m int) int {
	if m == 1 {
		return 0
	}
	res := 1
	a %= m
	for b > 0 {
		if b&1 == 1 {
			res = res * a % m
		}
		a = a * a % m
		b >>= 1
	}
	return res
}

// towerMod - recursively evaluates the power tower modulo a small number
// instead of ever constructing the huge integer.
func towerMod(a []int, mod int) int {
	if mod == 1 {
		return 0
	}
	if len(a) == 0 {
		return 1
	}
	if len(a) == 1 {
		return a[0] % mod
	}

	p := phi(mod)
	e := towerMod(a[1:], p)

	// Detect whether the real exponent is at least phi(mod).
	big := false
	if len(a) > 2 || a[1] >= p {
		big = true
	}

	if big {
		e += p
	}

	return powMod(a[0], e, mod)
}

func LastDigit(as []int) int {
	if len(as) == 0 {
		return 1
	}

	return towerMod(as, 10)
}
