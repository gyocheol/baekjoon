import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int first = 666;

        while (n != 0) {
            if (String.valueOf(first).contains("666")) {
                n--;
                if (n == 0) {
                    break;
                }
            }
            first++;
        }
        System.out.println(first);
    }
}