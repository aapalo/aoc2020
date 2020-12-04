package main

import (
  "fmt"
  "bufio"
  "log"
  "os"
  "strings"
  "strconv"
)

var (
  // 1, 2 or 3
  part int = 1
  sample bool = false
)

func helper(val int) int {
  if sample {
    return 1
  } else {
    return 0
  }
}

func counter(w string, ch string) (c int) {
  c = 0
  for _, v := range w {
    if string(v) == (ch) {
      c += 1
    }
  }
  return
}

func partone(s []string) (ans int) {
  ans = 0
  //var i []string
  var char string
  //fmt.Println(s)
  for _, v := range s {
    //fmt.Println("Part two:", v)
    i := strings.Split(v, " ")
    j := strings.Split(i[0], "-")
    low, _ := strconv.Atoi(j[0])
    high, _ := strconv.Atoi(j[1])
    char = string(i[1][0])
    word := string(i[2])
    c := counter(word, char)
    if (low <= c) && (c <= high) {
      ans += 1
    }
    //fmt.Println(i, low, high, char, word)
  }

  fmt.Println("Part one:", ans)
  return ans
}

func parttwo(s []string) (ans int) {
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
  var s []string
  scanner := bufio.NewScanner(file)
  for scanner.Scan() {
    s = append(s, scanner.Text())
    //fmt.Println(scanner.Text())
  }
  //fmt.Println(scanner)
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
