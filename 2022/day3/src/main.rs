fn find_common_character(a: String, b: String) -> char {
    for c in a.chars() {
        if b.contains(c) {
            return c;
        }
    }
    return ' ';
}

fn find_common_character_3(s1: String, s2: String, s3: String) -> char {
    for c in s1.chars() {
        if s2.contains(c) && s3.contains(c) {
            return c;
        }
    }
    return ' ';
}

fn get_value(c: char) -> i32 {
    if 'a' <= c && c <= 'z' {
        c as i32 - 'a' as i32 + 1
    } else {
        c as i32 - 'A' as i32 + 27
    }
}

fn main() {
    let stdin = std::io::stdin();
    let mut total_score = 0;
    let lines: Vec<String> = stdin
        .lines()
        .map(|line| line.expect("").trim().to_string())
        .collect();
    let lines_copy = lines.to_vec();
    for line in lines {
        let length = line.len();
        let (first_half, second_half) = line.split_at(length / 2);
        let common_character =
            find_common_character(first_half.to_string(), second_half.to_string());
        total_score += get_value(common_character);
    }

    let mut second_total = 0;
    for idx in (0..lines_copy.len()).step_by(3) {
        let s1 = lines_copy[idx].to_string();
        let s2 = lines_copy[idx + 1].to_string();
        let s3 = lines_copy[idx + 2].to_string();
        let common_character = find_common_character_3(s1, s2, s3);
        second_total += get_value(common_character);
    }
    println!("Total score: {total_score}");
    println!("Total score 2: {second_total}");
}
