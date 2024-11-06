import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int num = Integer.parseInt(st.nextToken());

        if (num%10 == 0){
            int a = num / 100;
            int b = num % 100;
            System.out.println(a + b);
        }
        else {
            int a = num / 10;
            int b = num % 10;
            System.out.println(a + b);
        }
    }
}
