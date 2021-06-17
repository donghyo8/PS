import java.util.HashMap;

public class Main14425_ {
    public static void main(String[] args) {
        int count = 0;
        String[] target = { "baekjoononlinejudge", "startlink", "codeplus", "sundaycoding", "codingsh" };
        String[] arr = { "baekjoon", "codeplus", "codeminus", "startlink", "starlink", "sundaycoding", "codingsh",
                "codinghs", "sondaycoding", "startrink", "icerink" };

        HashMap<String, Integer> map = new HashMap<>();

        for (int i = 0; i < target.length; i++) {
            map.put(target[i], 1);
        }

        for (int i = 0; i < arr.length; i++) {
            String str = arr[i];
            if (map.get(str) != null) {
                count++;
            }
        }
        System.out.println(count);

    }
}