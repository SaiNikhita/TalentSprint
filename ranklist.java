import java.io.*;
import java.util.*;
import java.util.stream.*;

public class ranklist {
	
	
	
	public static void main(String[] args) throws IOException {

		BufferedReader abc = new BufferedReader(new FileReader("C:\\Users\\Anudeep\\PycharmProjects\\TalentSprint\\marklist.txt"));
		Map<String, Integer> students = new HashMap<>();
		String line;
		while((line = abc.readLine()) != null) {
			String [] student = line.split(" ");
			students.put(student[0], Integer.parseInt(student[1]));
		}
		abc.close();
		Map<String, Integer> sorted = students
		        .entrySet()
		        .stream()
		        .sorted(Collections.reverseOrder(Map.Entry.comparingByValue()))
		        .collect(
		            Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue, (e1, e2) -> e2,
		                LinkedHashMap::new));
		int rank = 1;
		for (Map.Entry<String,Integer> entry : sorted.entrySet())  
            System.out.println(toString(rank) + entry.getKey()
                              + entry.getValue());
	}

}
