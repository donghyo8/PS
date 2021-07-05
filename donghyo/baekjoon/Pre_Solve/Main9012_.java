import java.util.Stack;

public class Main9012_ {
    public static void main(String[] args) {
        String input = "()()()()(()()())()";
        char[] arr = input.toCharArray();
        Func call = new Func();
        call.solution(arr);
    }
}

class Func {
    public void solution(char[] arr) {
        Stack<Character> st = new Stack<Character>();

        for (int i = 0; i < arr.length; i++) {
            if (st.empty()) {
                if (arr[i] == '(') {
                    st.push(arr[i]);
                } else {
                    System.out.print("NO");
                    break;
                }
            } else if (arr[i] == '(') {
                st.push(arr[i]);
            } else if (arr[i] == ')') {
                st.pop();
            }
        }
        if (st.empty()) {
            System.out.println("YES");

        } else {
            System.out.println("NO");
        }

    }

}
