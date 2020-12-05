package main

import (
  "fmt"
  "bufio"
  "log"
  "os"
  "strconv"
)

var (
  // 1, 2 or 3
  part int = 3
  sample bool = true
)

func helper(val int) int {
  if sample {
    return 1
  } else {
    return 0
  }
}

func partone(s []int) (ans int) {
  ans = 1
  fs := 0

  for _, v := range s {
    fs += v
  }
  
  fmt.Println("Part one:", ans)
  return ans
}

func parttwo(s []int) (ans int) {
  ans = 2
  fmt.Println("Part two:", ans)
  return ans
}

func main() {
  var filename string = "./input.txt"
  if sample {
    filename = "./sample.txt"
  }
  file, err := os.Open(filename)
  if err != nil {
    log.Fatal(err)
  }
  defer file.Close()
  var s []int
  var t string
  scanner := bufio.NewScanner(file)
  for scanner.Scan() {
    t = scanner.Text()
    if n, err := strconv.Atoi(t); err == nil {
      s = append(s, n)
    } else {
      fmt.Println(t, "is not an integer.")
    }
    //fmt.Println(s)
  }
  if err := scanner.Err(); err != nil {
    log.Fatal(err)
  }
  //var fuelsum int = 0
  if part == 1 {
    partone(s)
  } else if part == 2 {
    parttwo(s)
  } else {
    partone(s)
    parttwo(s)
  }
}
