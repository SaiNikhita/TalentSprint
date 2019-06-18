
public class isPanagram {

	public static boolean is_panagram(String input) {
		int[] letter_frequency = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		char[] input_str = input.toLowerCase().toCharArray();
		for(int i = 0; i <input_str.length; i++) {
	        if(input_str[i] != ' '){
	            letter_frequency[input_str[i] % 97] += 1;
	        }
		}
		for(int i = 0; i <26; i++) {
			if(letter_frequency[i] == 0){
				return false;
	        }
		}
		return true;
	}
	

	public static void main(String[] args) {
		String input = "Pack my box with five dozen liquor jugs";
		System.out.println(is_panagram(input));
	}

}
