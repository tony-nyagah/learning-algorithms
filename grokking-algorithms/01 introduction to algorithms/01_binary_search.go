package main

import (
	"fmt"
)

func binarySearch(arr []int, target int) int {
	low := 0
	high := len(arr) - 1

	for low <= high {
		mid := (low + high) / 2

		if arr[mid] == target {
			return mid
		}

		if arr[mid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}

	return -1
}

func main() {
	fmt.Println(binarySearch([]int{1, 3, 5, 7, 9}, 7))
	fmt.Println(binarySearch([]int{1, 3, 5, 7, 9}, -1))
}
