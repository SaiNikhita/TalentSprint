
public class Assessment4 {
	
	public static int[] terminus(int[] point, String[] steps) {
		for( int i = 0; i < steps.length; i++ ) {
			String direction = "";
			int num_of_step;
			String[] directions = steps[i].split("[0-9]");
			String[] num_of_steps = steps[i].split("[NSWE]");
			for( int j = 0; i < directions.length; i++ ) {
				if(directions[j] != ""){
						direction = directions[j];
				}
			}
			for( int j = 0; i < num_of_steps.length; i++ ) {
				if(num_[j] != ""){
						direction = directions[j];
				}
			}
		}
		return point;
	}

	public static void main(String[] args) {
		Assessment4 a = new Assessment4();
		String[] steps = {"1N", "3NW"};
		int[] point = {1,1};
		int[] new_lattice = a.terminus(point, steps);
		System.out.println(new_lattice);
	}

}
