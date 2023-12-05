use std::io::{self, BufReader};
use std::io::prelude::*;
use std::fs::File;
use std::str::FromStr;

fn main() -> io::Result<()> {
    let file = File::open("src/input.txt")?;
    let reader = BufReader::new(file);
    let mut result = 0;

    for line in reader.lines() {
        let default_number = char::default();
        let mut first_number = char::default();
        let mut last_number = char::default();
        for char in line.unwrap().chars() {
            if char.is_numeric()  {
                if first_number.eq(&default_number){
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
    Ok(())
}