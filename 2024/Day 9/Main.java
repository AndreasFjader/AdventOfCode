import java.io.IOException;
import java.math.BigInteger;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Main {
    private static final int EMPTY_SPACE = -1;

    public static void main(String[] args) {
        String testInput = readFromFile("test.txt");
        String actualInput = readFromFile("input.txt");

        System.out.println("Part 1: " + part1(testInput));
        System.out.println("Part 1: " + part1(actualInput));
        System.out.println("Part 2: " + part2(testInput));
        System.out.println("Part 2: " + part2(actualInput));
    }

    static BigInteger part1(String input) {
        return calculateSum(rearrangeBits(parseInput(input)));
    }

    static BigInteger part2(String input) {
        return calculateSum(rearrangeEntireFiles(parseInput(input)));
    }

    // Actual logic below
    private static BigInteger calculateSum(List<Integer> result) {
        BigInteger sum = new BigInteger("0");
        for (int i = 0; i < result.size(); i++) {
            if (result.get(i) == EMPTY_SPACE) continue;

            long value = result.get(i) * i;
            sum = sum.add(BigInteger.valueOf(value));
        }

        return sum;
    }

    static List<Integer> rearrangeEntireFiles(List<Integer> data) {
        List<Integer> result = new ArrayList<>(data);
        
        for (int i = data.size() - 1; i >= 0; i--) {
            int val = data.get(i);
            if (val == EMPTY_SPACE) {
                continue;
            }

            // We have a file, get its size, then find the first available empty space to the left.
            int di = i;
            int v = val;

            while (di >= 0 && result.get(di) == v) {
                di--;
            }

            int fileSize = i - di;

            // Now find the first available empty space.
            for (int j = 0; j < i; j++) {
                if (result.get(j) != EMPTY_SPACE) continue; // Not interesting

                // Check if the empty space is big enough
                int jtmp = j;
                while (jtmp < result.size() && result.get(jtmp) == EMPTY_SPACE) {
                    jtmp++;
                }

                int freeSpace = jtmp - j;

                if (freeSpace >= fileSize) {
                    int freeSpaceStart = j;
                    int fileStart = i - fileSize + 1;

                    for (int k = 0; k < fileSize; k++) {
                        result.set(freeSpaceStart + k, v);
                        result.set(fileStart + k, EMPTY_SPACE);
                    }
                    break;
                }
            }
            i -= fileSize - 1;
        }

        return result;
    }

    static List<Integer> rearrangeBits(List<Integer> chars) {
        int rightPointer = chars.size() - 1;
        List<Integer> result = new ArrayList<>(chars);
        for (int i = 0; i < result.size(); ++i) {
            if (result.get(i) != EMPTY_SPACE) continue;

            while (result.get(rightPointer) == EMPTY_SPACE) {
                rightPointer--;
            }

            if (rightPointer < i) {
                break;
            }

            // Rearrange
            result.set(i, result.get(rightPointer));
            result.set(rightPointer, EMPTY_SPACE);
        }
        return result;
    }

    static List<Integer> parseInput (String input) {
        List<Integer> result = new ArrayList<>();
        boolean isFile = true;
        int id = 0;
        for (char c : input.toCharArray()) {
            for (int i = 0; i < Character.getNumericValue(c); i++) {
                result.add(isFile ? id : EMPTY_SPACE);
            }

            // Ugly flippn
            if (isFile) id++;
            isFile = !isFile;
        }
        return result;
    }

    static String readFromFile(String path) {
        try {
            return new String(Files.readAllBytes(Paths.get(path)));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
