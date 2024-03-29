use std::fs;

fn main() {
    a();
    b();
}

fn a() {
    let contents =
        fs::read_to_string("../input/day_1.txt").expect("Something went wrong reading the file");

    let calories_per_elf: Vec<u32> = contents
        .trim()
        .split("\n\n")
        .map(combine_calories)
        .collect::<Result<_, _>>()
        .expect("Input parse error");

    println!("{}", calories_per_elf.iter().max().unwrap());
}

fn b() {
    let contents =
        fs::read_to_string("../input/day_1.txt").expect("Something went wrong reading the file");

    let mut calories_per_elf: Vec<u32> = contents
        .trim()
        .split("\n\n")
        .map(combine_calories)
        .collect::<Result<_, _>>()
        .expect("Input parse error");

    // Admittedly sorting is a lazy way
    calories_per_elf.sort_by(|a, b| b.cmp(a));
    println!("{}", calories_per_elf.iter().take(3).sum::<u32>())
}

fn combine_calories(value: &str) -> Result<u32, std::num::ParseIntError> {
    value.lines().map(|s| s.parse::<u32>()).sum()
}
