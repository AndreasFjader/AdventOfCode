using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Robot(int x, int y, int vx, int vy)
{
    public int X { get; set; } = x;
    public int Y { get; set; } = y;
    public int VX { get; set; } = vx;
    public int VY { get; set; } = vy;
}

class Program {
    static void Main(string[] args) {
        var testInput = File.ReadAllLines("test.txt");
        var actualInput = File.ReadAllLines("input.txt");

        Console.WriteLine($"Part 1 (test): {Part1(testInput, 11, 7, 100)}");
        Console.WriteLine($"Part 1 (actual): {Part1(actualInput, 101, 103, 100)}");
        // Test data didn't seem to contain a christmas tree.
        Console.WriteLine($"Part 2 (actual): {Part2(actualInput, 101, 103)}");
    }

    static int Part1(string[] input, int gx, int gy, int seconds)
    {
        var robots = ParseInput(input);
        for (int i = 0; i < seconds; i++)
        {
            MoveRobots(robots, gx, gy);
        }

        return CountRobotsInEachQuadrant(robots, gx, gy);
    }

    static int Part2(string[] input, int gx, int gy)
    {
        var robots = ParseInput(input);
        int seconds = 0;

        while (true)
        {
            seconds++;
            MoveRobots(robots, gx, gy);
            if (NoRobotsOverlap(robots))
            {
                // PrintGrid(robots, gx, gy);
                return seconds;
            }
        }
    }

    // Logic

    static bool NoRobotsOverlap(List<Robot> robots) => 
        robots
            .GroupBy(robot => (robot.X, robot.Y))
            .All(group => group.Count() == 1);

    static bool IsWithinQuadrant(Robot robot, int ul, int ur, int bl, int br) => 
        robot.X >= ul && robot.X <= ur && robot.Y >= bl && robot.Y <= br;

    static void MoveRobots(List<Robot> robots, int gx, int gy)
    {
        foreach (var robot in robots)
        {
            robot.X = ((robot.X + robot.VX) % gx + gx) % gx;
            robot.Y = ((robot.Y + robot.VY) % gy + gy) % gy;
        }
    }

    static int CountRobotsInEachQuadrant(List<Robot> robots, int gx, int gy)
    {
        int topLeft = 0, 
            topRight = 0, 
            bottomLeft = 0, 
            bottomRight = 0,
            midX = gx / 2,
            midY = gy / 2;
        foreach (var robot in robots)
        {
            // Offsetting the grid by 1 to ignore the middle
            if (IsWithinQuadrant(robot, midX + 1, gx, midY + 1, gy))
            {
                topRight++;
            }
            else if (IsWithinQuadrant(robot, 0, midX - 1, midY + 1, gy))
            {
                topLeft++;
            }
            else if (IsWithinQuadrant(robot, midX + 1, gx, 0, midY - 1))
            {
                bottomRight++;
            }
            else if (IsWithinQuadrant(robot, 0, midX - 1, 0, midY - 1))
            {
                bottomLeft++;
            }
        }

        return topLeft * topRight * bottomLeft * bottomRight;
    }


    // Input parsing

    static List<Robot> ParseInput(string[] input)
    {
        List<Robot> robots = [];

        foreach (var line in input)
        {
            var parts = line.Split(" ");
            var (X, Y) = ExtractRobotData(parts[0]);
            var (VX, VY) = ExtractRobotData(parts[1]);
            robots.Add(new Robot(X, Y, VX, VY));
        }

        return robots;
    }

    static (int, int) ExtractRobotData(string data)
    {
        var parts = data.Split("=")[1].Split(",");
        return (int.Parse(parts[0]), int.Parse(parts[1]));
    }

    // Debugging
    static void PrintGrid(List<Robot> robots, int gx, int gy)
    {
        char[,] grid = new char[gx, gy];
        foreach (var robot in robots)
        {
            grid[robot.X, robot.Y] = '#';
        }

        for (int y = 0; y < gy; y++)
        {
            for (int x = 0; x < gx; x++)
            {
                Console.Write(grid[x, y] == '#' ? '#' : ' ');
            }
            Console.WriteLine();
        }
    }
}
