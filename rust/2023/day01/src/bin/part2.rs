use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;
use std::str::FromStr;

fn main() -> () {
    let result = part2("src/part2/input.txt");
    println!("Result is: {}", result);
    return;
}
fn part2(input: &str) -> i32 {
    let file = File::open(input);
    let reader = BufReader::new(file.unwrap());
    let mut result = 0;
    let numbers_as_strings = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    ];

    for line in reader.lines() {
        let mut line = line.unwrap();
        let default_number = char::default();
        let mut first_number = char::default();
        let mut last_number = char::default();
        for number in 0..=9 {
                // replace words with actual numbers
                line = line.replace(numbers_as_strings[number], number.to_string().as_str())
        };
        for char in line.chars() {
            if char.is_numeric() {
                if first_number.eq(&default_number) {
                    first_number = char;
                }
                last_number = char;
            }
        }
        let mut number = String::new();
        number.push(first_number);
        number.push(last_number);
        result += i32::from_str(&number).unwrap();
    }
    println!("{}", result);
    return result;
}

#[cfg(test)]
mod tests {
    use crate::part2;

    #[test]
    fn it_works() {
        let result = part2("src/part2/test-input.txt");
        assert_eq!(result, 281);
    }
}
