using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Program {
    static void Main(string[] args) 
    {
        var testInput = File.ReadAllText("test.txt");
        var actualInput = File.ReadAllText("input.txt");
        
        Console.WriteLine($"Part 1 (test): {Part1(testInput)}");
        Console.WriteLine($"Part 1 (actual): {Part1(actualInput)}");
        Console.WriteLine($"Part 2 (test): {Part2(testInput)}");
        Console.WriteLine($"Part 2 (actual): {Part2(actualInput)}");
    }
    
    static long Part1(string input) 
    {
        var (patterns, desiredPatterns) = ParseInput(input);
        return desiredPatterns.Sum(desired => FindPattern(desired, patterns));
    }
    
    static long Part2(string input) 
    {
        var (patterns, desiredPatterns) = ParseInput(input);
        return desiredPatterns.Sum(desired => FindPattern(desired, patterns, true));
    }
    
    static long FindPattern(string desired, HashSet<string> patterns, bool isPart2 = false)
    {
        long[] dp = new long[desired.Length + 1];
        dp[0] = 1;
        
        for (int o = 1; o <= desired.Length; ++o)
        {
            for (int i = 0; i < o; ++i)
            {
                if (dp[i] > 0 && patterns.Contains(desired[i..o]))
                {
                    if (isPart2)
                    {
                        dp[o] += dp[i];
                    }
                    else
                    {
                        dp[o] = 1;
                        break;
                    }
                }
            }
        }
        
        return dp[desired.Length];
    }
    
    // Helpers
    
    static (HashSet<string> patterns2, string[] desired) ParseInput(string input) 
    {
        
        HashSet<string> patterns = [.. input.Split("\n\n")[0].Split(", ")];
        string[] desired = input.Split("\n\n")[1].Split("\n");
        
        return (patterns, desired);
    }
}
