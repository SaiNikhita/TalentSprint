import java.util.Arrays;

public class rock_paper_scissors {
	public static void evaluate_winner(String input) {
		String[] rounds = input.split(",");
		String[] winner_cases = {"RS", "SP", "PR"};
		int won = 0;
		int lost = 0;
		int draw = 0;
		for(int i = 0; i < rounds.length; i++ ) {
			System.out.println(rounds[i]);
			if (rounds[i].charAt(0) == rounds[i].charAt(1)) {
				draw += 1;
			}
			else if(Arrays.asList(winner_cases).contains(winner_cases)[i]) {
				won += 1;
			}
			else {
				lost += 1;
			}
		}
		System.out.println(won);
		System.out.println(lost);
		System.out.println(draw);
	}
	

	public static void main(String[] args) {
		String input = new String("RP,RR,SP,SR");
		evaluate_winner(input);

	}

}
