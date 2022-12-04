type Interval = (i32, i32);

fn parse_interval(s: &str) -> Interval {
    let tokens: Vec<&str> = s.split('-').collect();
    (tokens[0].parse().unwrap(), tokens[1].parse().unwrap())
}

fn get_intersection(a: Interval, b: Interval) -> Interval {
    (std::cmp::max(a.0, b.0), std::cmp::min(a.1, b.1))
}

fn is_non_empty(a: Interval) -> bool {
    a.0 <= a.1
}

fn contains(a: Interval, b: Interval) -> bool {
    a.0 >= b.0 && a.1 <= b.1
}

fn main() {
    let stdin = std::io::stdin();
    let mut num_contained = 0;
    let mut num_overlap = 0;
    for line in stdin.lines() {
        let line = line.unwrap();
        let tokens: Vec<&str> = line.split(',').collect();
        let interval1 = parse_interval(tokens[0]);
        let interval2 = parse_interval(tokens[1]);
        if contains(interval2, interval1) || contains(interval1, interval2) {
            num_contained += 1;
        }
        if is_non_empty(get_intersection(interval1, interval2)) {
            num_overlap += 1;
        }
    }
    println!("Result: {num_contained}");
    println!("Overlap: {num_overlap}");
}
