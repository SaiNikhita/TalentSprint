public class Date {
	public static boolean is_ambiguous(String date) {
		String[] date_list = date.split("/");
		return Integer.parseInt(date_list[0]) <= 12 && Integer.parseInt(date_list[1]) <= 12;
	}
	
	public static void main(String args[]) {
		String date = new String("01/02/1999");
		System.out.println(is_ambiguous(date));
	}
}
