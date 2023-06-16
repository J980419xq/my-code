package main

/*
矩阵快速幂模板
const mod int = 1e9 + 7
func pow(matrix [][]int, x int) [][]int{
	m, n := len(matrix), len(matrix[0])
	ret := make([][]int, m)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i == j {
				ret[i] = append(ret[i], 1)
			} else {
				ret[i] = append(ret[i], 0)
			}
		}
	}
	for x > 0 {
		if x & 1 == 1 {
			ret = mul(ret, matrix)
		}
		x >>= 1
		matrix = mul(matrix, matrix)
	}
	return ret
}
func mul(a [][]int, b [][]int) [][]int{
	m, n, p := len(a), len(a[0]), len(b[0])
	ret := make([][]int, m)
	for i := 0; i < m; i++ {
		ret[i] = make([]int, p)
	}
	fmt.Println(ret)
	for i := 0; i < m; i++ {
		for j := 0; j < p; j++ {
			for k := 0; k < n; k++ {
				ret[i][j] = (ret[i][j] + (a[i][k] * b[k][j]) % mod) % mod
			}
		}
	}
	return ret
}*/

/*
线段树模板(区间和)
struct
*/

/*
最大公因数
func _gcd(a, b int) int {
	for a != 0 {
		a, b = b%a, a
	}
	return b
}
func gcd(nums []int) int {
	g := 0
	for _, x := range nums {
		g = _gcd(g, x)
	}
	return g
}*/

/*快速幂取余a^b%c
func PowerMod(a, b, c int) int {
    ans := 1
    a = a % c
    for b > 0 {
        if b % 2 == 1 {
            ans = (ans * a) % c
        }
        b = b/2
        a = (a * a) % c
    }
    return ans
}*/
import (
	"fmt"
	"log"
	"os"
	"strings"
	"sync"

	"example.com/greetings"
)

var wg sync.WaitGroup

func hello() {
	defer wg.Done()
	fmt.Println("hello")
}
func main() {
	wg.Add(1)
	go hello()
	fmt.Println(os.Args[0])
	fmt.Println(strings.Join(os.Args[1:], " "))
	log.SetPrefix("greetings: ")
	log.SetFlags(0)
	message, err := greetings.Love("Yyh")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(message)
	wg.Wait()
}
