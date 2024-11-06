import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int defense = Integer.parseInt(st.nextToken());
        int ignore = Integer.parseInt(st.nextToken());

//        백분율을 구할 때는 double을 사용해야 할 것 같다.
//        100으로 나눴을 때 시멘틱 오류 발생 -> gpt 참고하여 문제 해결 => 100.0으로 뺌
        double rate = defense * (ignore / 100.0);
        double pureDefense = defense - rate;

        if (pureDefense >= 100) System.out.println(0);
        else System.out.println(1);
    }
}
