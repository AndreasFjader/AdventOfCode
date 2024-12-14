using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;

class Group(List<Plant> plants)
{
    public List<Plant> Plants { get; } = plants;
}

class Plant(int x, int y, char specie)
{
    public int X { get; } = x;
    public int Y { get; } = y;
    public char Specie { get; } = specie;

    public bool HasFenceOnTop { get; set; }
    public bool HasFenceOnRight { get; set; }
    public bool HasFenceOnBottom { get; set; }
    public bool HasFenceOnLeft { get; set; }

    public bool IsValidNeighbor(Plant neighbor)
    {
        return !Equals(neighbor) && IsNeighbor(neighbor) && IsSameSpecie(neighbor);
    }

    public bool IsNeighbor(Plant plant) 
    {
        return X == plant.X && Math.Abs(Y - plant.Y) == 1
            || Y == plant.Y && Math.Abs(X - plant.X) == 1;
    }

    public bool IsSameSpecie(Plant plant)
    {
        return Specie == plant.Specie;
    }

    public bool Equals(Plant obj)
    {
        return obj.X == X && obj.Y == Y && IsSameSpecie(obj);
    }
}

class Program {
    static void Main(string[] args) 
    {
        var testInput = File.ReadAllLines("test.txt");
        var actualInput = File.ReadAllLines("input.txt");

        Console.WriteLine($"Part 1 (test): {Part1(testInput)}"); // 1930
        Console.WriteLine($"Part 1 (actual): {Part1(actualInput)}");
        Console.WriteLine($"Part 2 (test): {Part2(testInput)}"); // 1206
        Console.WriteLine($"Part 2 (actual): {Part2(actualInput)}");
    }

    static long Part1(string[] garden)
    {
        List<Group> groups = GroupGardenPlots(garden);
        
        long totalPrice = 0;
        // Count the fence perimiter for each group.
        foreach (var group in groups) 
        {
            // This is inefficient because I'm re-checking each neighbor to their neighbors
            // I should keep track of which fences don't need to be counted, but alas.
            int totalFences = 0;
            foreach (var plant in group.Plants) 
            {
                int fenceCount = 4; // Start at 4 for each plant's corner, remove one for each neighbor in each direction
                foreach (var neighbor in group.Plants) 
                {
                    if (plant.IsNeighbor(neighbor) && !plant.Equals(neighbor))
                    {
                        fenceCount--;
                    }
                }
                totalFences += fenceCount;
            }

            totalPrice += totalFences * group.Plants.Count;
        }

        return totalPrice;
    }

    static long Part2(string[] garden) {
        List<Group> groups = GroupGardenPlots(garden);
        long totalPrice = 0;
        // Count the fence perimiter for each group.
        foreach (var group in groups)
        {
            totalPrice += CountFenceCostForPerimiterByNumberOfSides(group);
        }

        return totalPrice;
    }

    static long CountFenceCostForPerimiterByNumberOfSides(Group perimiter) 
    {
        long totalFences = 0;

        HashSet<(int, int)> fencePointLookup = [];
        foreach (var plant in perimiter.Plants) fencePointLookup.Add((plant.X, plant.Y));

        foreach (var plant in perimiter.Plants)
        {
            // If the plant has a vertical or horisontal neighbor only, it has no edge and is therefore the same fence.
            // If it has no neighbor horisontally or vertically, it has an edge in that direction.
            
            
        }


        return totalFences * perimiter.Plants.Count;
    }

    static List<Group> GroupGardenPlots(string[] garden) 
    {
        List<Plant> allPlants = [];
        for (int y = 0; y < garden.Length; y++) 
        {
            for (int x = 0; x < garden[y].Length; x++) 
            {
                allPlants.Add(new Plant(x, y, garden[y][x]) 
                {
                    // In part 2, this will be set to false if there's a neighbor in the direction
                    HasFenceOnTop = true,
                    HasFenceOnRight = true,
                    HasFenceOnBottom = true,
                    HasFenceOnLeft = true
                });
            }
        }

        List<Group> groups = [];
        HashSet<Plant> visited = [];
        foreach (var plant in allPlants) 
        {
            if (visited.Contains(plant)) continue;

            Group group = new Group([]);
            Queue<Plant> queue = new();
            queue.Enqueue(plant);
            visited.Add(plant);
            while (queue.Count > 0) 
            {
                var currentPlant = queue.Dequeue();
                group.Plants.Add(currentPlant);

                // Inefficient, but I don't care
                foreach (var potentialNeighbor in allPlants)
                {
                    if (currentPlant.IsValidNeighbor(potentialNeighbor) 
                        && !visited.Contains(potentialNeighbor))
                    {
                        queue.Enqueue(potentialNeighbor);
                        visited.Add(potentialNeighbor);
                    }
                }
            }

            groups.Add(group);
        }

        return groups;
    }
}
