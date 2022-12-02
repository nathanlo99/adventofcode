fn insert_into_leaderboard(leaderboard: &mut [i32; 3], amount: i32) -> () {
    let mut amount = amount;
    for i in 0..3 {
        if amount > leaderboard[i] {
            std::mem::swap(&mut amount, &mut leaderboard[i]);
        }
    }
}

fn main() -> () {
    let mut leaderboard: [i32; 3] = [-1; 3];
    let mut current_amount: i32 = 0;

    use std::io::BufRead;
    let stdin = std::io::stdin();
    for line in stdin.lock().lines() {
        let line = line.unwrap();
        if line.is_empty() {
            insert_into_leaderboard(&mut leaderboard, current_amount);
            current_amount = 0;
        } else {
            let num = line
                .trim()
                .parse::<i32>()
                .expect("Line did not contain a number");
            current_amount += num;
        }
    }
    insert_into_leaderboard(&mut leaderboard, current_amount);

    let max_amount: i32 = leaderboard[0];
    let sum_of_top_three: i32 = leaderboard.iter().sum();
    println!("Maximum amount:   {max_amount}");
    println!("Sum of top three: {sum_of_top_three}");
}
