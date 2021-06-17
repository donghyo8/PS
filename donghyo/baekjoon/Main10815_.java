import java.util.Arrays;

public class Main10815_ {
    public static void main(String[] args) {
        int[] numberList = { 6, 3, 2, 10, -10 };
        int[] targetList = { 10, 9, -5, 2, 3, 4, 5, -10 };
        int[] checkList = { 0, 0, 0, 0, 0, 0, 0, 0 };
        Arrays.sort(numberList);

        for (int idx = 0; idx < targetList.length; idx++) {
            int left = 0, right = numberList.length, mid = 0;

            while (left <= right) {
                mid = (left + right) / 2;

                if (numberList[mid] == targetList[idx]) {
                    checkList[idx] += 1;
                    break;
                } else if (numberList[mid] > targetList[idx]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
        }
        for (int i : checkList) {
            System.out.print(i + " ");
        }
    }
}
