import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        String testInput = readFromFile("test.txt");
        String actualInput = readFromFile("input.txt");

        System.out.println("Part 1 (test): " + resolve(testInput, 25));
        System.out.println("Part 1 (actual): " + resolve(actualInput, 25));
        System.out.println("Part 2 (test): " + resolve(testInput, 75));
        System.out.println("Part 2 (actual): " + resolve(actualInput, 75));
    }

    static long resolve(String stones, int blinks) {
        long total = 0;
        Map<String, Long> cache = new HashMap<>();
        for (String stone : stones.split(" ")) {
            total += solve(stone, blinks, cache);
        }
        return total;
    }

    static long solve(String stone, int blinksRemaining, Map<String, Long> cache) {
        
        String key = stone + ":" + blinksRemaining;
        if (blinksRemaining <= 0) {
            return 1;
        }

        if (cache.containsKey(key)) {
            return cache.get(key);
        }

        long result;
        if (stone.equals("0")) {
            result = solve("1", blinksRemaining - 1, cache);
        } else if (stone.length() % 2 == 0) {
            String left = String.valueOf(Long.parseLong(stone.substring(0, stone.length() / 2)));
            String right = String.valueOf(Long.parseLong(stone.substring(stone.length() / 2)));
            result = solve(left, blinksRemaining - 1, cache) + solve(right, blinksRemaining - 1, cache);
        } else {
            result = solve(String.valueOf(Long.parseLong(stone) * 2024), blinksRemaining - 1, cache);
        }

        cache.putIfAbsent(key, result);
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
