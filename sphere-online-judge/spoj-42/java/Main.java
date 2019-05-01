import java.util.Scanner;

public class Main {
	static final int FORTY_TWO = 42;
	static final Boolean NO_HAS_BREAK = true;


	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int currentNumber;

		while(NO_HAS_BREAK){
				currentNumber = scanner.nextInt();

				if(currentNumber == FORTY_TWO) break;
				System.out.println(currentNumber);
				if(!scanner.hasNext()) break;
		}
	}


}
