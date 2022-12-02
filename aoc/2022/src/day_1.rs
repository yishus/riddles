use std::fs;

pub fn a() {
    let contents =
        fs::read_to_string("input/day_1.txt").expect("Something went wrong reading the file");
}
