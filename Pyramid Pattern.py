def print_spaces(n):
    size = 50
    for i in range(0, size - n):
        print(" ", end="")


def print_chars(n, char):
    for i in range(0, n):
        if i % 2 != 0:
            print(" ", end="")
        else:
            print(char, end="")


def print_row_of_pyramid(row_num, num_of_rows, char):
    num_of_chars = 2 * row_num + 1
    print_spaces(num_of_chars//2 + 1)
    print_chars(num_of_chars, char)
    print()


def print_pyramid(num_of_rows, char):
    for row in range(0, num_of_rows):
        print_row_of_pyramid(row, num_of_rows, char)


num_of_rows = 5
char = '*'
print_pyramid(num_of_rows, char)



"""
public class Pyramid {
	final static String STAR = "*";
	final static String SPACE = " ";
	final static String CRLF = "\n";
	final static int WIDTH = 30;

	final static String SP = STAR;
	final static String RP = STAR + STAR;
	final static String EP = CRLF;

	public static void main(String[] args) {
		int SIZE = Integer.parseInt(args[0]);

		System.out.println(pyramid(SIZE));
	}

	public static String pyramid(int n) {
		String pyramid = "";
		for (int lineNum = 0; lineNum < n; ++lineNum) {
			pyramid += line(lineNum);
		}
		return pyramid;
	}

	public static String line(int n) {
		return leftmargin(n) +
			startPattern(n) +
			repeatPattern(n) +
			endPattern(n);
	}
	public static String leftmargin(int n) {
		String margin = "";
		for (int i = 0; i < WIDTH - n; ++i) {
			margin += SPACE;
		}
		return margin;
	}

	public static String startPattern(int n) {
		return SP;
	}

	public static String repeatPattern(int n) {
		String rp = "";
		for (int i = 0; i < n; ++i) {
			rp += RP;
		}
		return rp;
	}

	public static String endPattern(int n) {
		return EP;
	}
}

"""