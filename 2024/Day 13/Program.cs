using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net.Security;

record Instruction(int AX, int AY, int BX, int BY, long PrizeX, long PrizeY);

class Program {
    static void Main(string[] args) {
        var testInput = File.ReadAllLines("test.txt");
        var actualInput = File.ReadAllLines("input.txt");

        Console.WriteLine($"Part 1 (test): {Solve(testInput, false)}");
        Console.WriteLine($"Part 1 (actual): {Solve(actualInput, false)}");
        Console.WriteLine($"Part 2 (test): {Solve(testInput, true)}");
        Console.WriteLine($"Part 2 (actual): {Solve(actualInput, true)}");
    }

    private static decimal Solve(string[] input, bool isPart2)
    {
        return ParseInstructions(input, isPart2)
            .Select(GetTokenCountForInstruction)
            .Where(IsValidTokenCount)
            .Sum();
    }

    private static bool IsValidTokenCount(decimal value) => value != decimal.MaxValue;

    private static decimal CalculateTokenCount(decimal countA, decimal countB) => countA * 3 + countB;

    private static bool AreButtonPressCountsIntegers(decimal countA, decimal countB) => countA % 1 == 0 && countB % 1 == 0;

    private static decimal GetTokenCountForInstruction(Instruction instruction)
    {
        var (AX, AY, BX, BY, PX, PY) = instruction;

        // ChatGPT had a lot of fun teaching me linear algebra for this one...
        decimal countA = (decimal) (PX * BY - PY * BX) / (AX * BY - AY * BX);
        decimal countB = (PX - AX * countA) / BX;

        return AreButtonPressCountsIntegers(countA, countB) 
            ? CalculateTokenCount(countA, countB) 
            : decimal.MaxValue;
    }

    private static List<Instruction> ParseInstructions(string[] input, bool isPart2) 
    {
        List<Instruction> instructions = [];
        for (int i = 0; i < input.Length; i+=4) 
        {
            var line1 = input[i].Split("X+")[1];
            var line2 = input[i+1].Split("X+")[1];
            var line3 = input[i+2].Split("X=")[1];

            var ax = int.Parse(line1.Split(", ")[0].Trim());
            var ay = int.Parse(line1.Split("Y+")[1].Trim());
            var bx = int.Parse(line2.Split(", ")[0].Trim());
            var by = int.Parse(line2.Split("Y+")[1].Trim());
            var px = isPart2 
                ? int.Parse(line3.Split(", ")[0].Trim()) + 10000000000000 
                : int.Parse(line3.Split(", ")[0].Trim());
            var py = isPart2 
                ? int.Parse(line3.Split("Y=")[1].Trim()) + 10000000000000
                : int.Parse(line3.Split("Y=")[1].Trim());

            instructions.Add(new Instruction(ax, ay, bx, by, px, py));
        }

        return instructions;
    }
}
