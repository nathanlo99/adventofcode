/*
                [V]     [C]     [M]
[V]     [J]     [N]     [H]     [V]
[R] [F] [N]     [W]     [Z]     [N]
[H] [R] [D]     [Q] [M] [L]     [B]
[B] [C] [H] [V] [R] [C] [G]     [R]
[G] [G] [F] [S] [D] [H] [B] [R] [S]
[D] [N] [S] [D] [H] [G] [J] [J] [G]
[W] [J] [L] [J] [S] [P] [F] [S] [L]
 1   2   3   4   5   6   7   8   9
*/

fn main() {
    let stdin = std::io::stdin();
    let mut stacks: [Vec<char>; 9] = [
        vec!['W', 'D', 'G', 'B', 'H', 'R', 'V'],
        vec!['J', 'N', 'G', 'C', 'R', 'F'],
        vec!['L', 'S', 'F', 'H', 'D', 'N', 'J'],
        vec!['J', 'D', 'S', 'V'],
        vec!['S', 'H', 'D', 'R', 'Q', 'W', 'N', 'V'],
        vec!['P', 'G', 'H', 'C', 'M'],
        vec!['F', 'J', 'B', 'G', 'L', 'Z', 'H', 'C'],
        vec!['S', 'J', 'R'],
        vec!['L', 'G', 'S', 'R', 'B', 'N', 'V', 'M'],
    ];
    for line in stdin.lines() {
        let line = line.unwrap();
        let tokens: Vec<&str> = line.split(' ').collect();
        let amount: usize = tokens[1].parse::<usize>().expect("Expected number");
        let source: usize = tokens[3].parse::<usize>().expect("Expected number") - 1;
        let target: usize = tokens[5].parse::<usize>().expect("Expected number") - 1;

        let mut tmp: Vec<char> = Vec::new();
        for _ in 0..amount {
            let top = stacks[source].pop().expect("Nothing to pop");
            tmp.push(top);
        }
        for _ in 0..amount {
            let top = tmp.pop().expect("Nothing to pop");
            stacks[target].push(top);
        }
    }
    for i in 0..9 {
        print!("{}", stacks[i].last().expect("Empty stack"));
    }
    println!("");
}
