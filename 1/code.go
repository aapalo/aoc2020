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
  sample bool = false
)

func helper(val int) int {
  if sample {
    return 1
  } else {
    return 0
  }
}

func partone(s []int) (ans int) {
  for _, i := range s {
    for _, j := range s {
      if i != j {
        if (i + j) == 2020 {
          ans = i * j
          //fmt.Println(i, j, ans)
        }
      }
    }
  }
  fmt.Println("Part one:", ans)
  return
}

func parttwo(s []int) (ans int) {
  for _, i := range s {
    for _, j := range s {
      for _, k := range s {
        if ((i!=j) && (j!=k) && (i!=k)) {
          if (i + j + k) == 2020 {
            ans = i * j * k
            //fmt.Println(i, j, k, ans)
            fmt.Println("Part two:", ans)
            return
          }
        }
      }
    }
  }
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
  }
  if err := scanner.Err(); err != nil {
    log.Fatal(err)
  }
  if part == 1 {
    partone(s)
  } else if part == 2 {
    parttwo(s)
  } else {
    partone(s)
    parttwo(s)
  }
}
