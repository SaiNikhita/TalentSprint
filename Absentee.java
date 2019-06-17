import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;
import java.util.stream.IntStream;

public class Absentee {
	public int sum_of_rollnums(List<Integer> rollnums) {
		return rollnums.stream().mapToInt(Integer::intValue).sum();
	}
	
    public static void main(String[] args) {
    	Absentee temp = new Absentee();
    	
    	int n=10;
        List<Integer> present_rollnums = Arrays.asList(1, 2, 3, 4,  6, 7, 8, 9, 10);
        int sum_of_present_rollnums = temp.sum_of_rollnums(present_rollnums);

        int sum_of_rollnums = n*(n+1)/2;
        		
        System.out.println(sum_of_rollnums - sum_of_present_rollnums);

    }

}