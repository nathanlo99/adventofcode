fn get_rps_score(opponent_move: i32, my_move: i32) -> i32 {
    const LOOKUP_TABLE: [[i32; 3]; 3] = [
        [3, 6, 0], // Opponent plays Rock
        [0, 3, 6], //                Paper
        [6, 0, 3], //                Scissors
    ];
    LOOKUP_TABLE[opponent_move as usize][my_move as usize]
}

fn get_score(opponent_move: i32, my_move: i32) -> i32 {
    get_rps_score(opponent_move, my_move) + my_move + 1
}

fn get_matching_move(opponent_move: i32, intended_result: i32) -> i32 {
    const LOOKUP_TABLE: [[i32; 3]; 3] = [[2, 0, 1], [0, 1, 2], [1, 2, 0]];
    LOOKUP_TABLE[opponent_move as usize][intended_result as usize]
}

fn main() {
    let stdin = std::io::stdin();
    let mut total_score = 0;
    for line in stdin.lines() {
        let line = line.unwrap();
        let tokens: Vec<&str> = line.split(' ').collect();
        let opponent_move = tokens[0].parse::<char>().unwrap() as i32 - 'A' as i32;
        let index = tokens[1].parse::<char>().unwrap() as i32 - 'X' as i32;
        let my_move = {
            // index
            get_matching_move(opponent_move, index)
        };
        let this_score = get_score(opponent_move, my_move);
        total_score += this_score;
    }
    println!("Total score: {total_score}");
}
