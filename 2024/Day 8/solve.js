// Advent of Code Day 8
import fs from 'fs';

function findAntinode(antenna1, antenna2) {
  const [x1, y1] = antenna1;
  const [x2, y2] = antenna2;

  return [2 * x1 - x2, 2 * y1 - y2];
}

function findAntinodes(antennaLocations) {
  const antinodes = [];
  for (let i = 0; i < antennaLocations.length; i++) {
    for (let j = 0; j < antennaLocations.length; j++) {
      const antenna1 = antennaLocations[i];
      const antenna2 = antennaLocations[j];

      if (antenna1[0] === antenna2[0] && antenna1[1] === antenna2[1]) {
        continue;
      }

      antinodes.push(findAntinode(antenna1, antenna2));
    }
  }
  return antinodes;
}

function getAntennaLocations(lines) {
  const antennaLocations = {};
  for (let i = 0; i < lines.length; i++) {
    for (let j = 0; j < lines[i].length; j++) {
      if (lines[i][j] !== '.') {
        if (!antennaLocations[lines[i][j]]) {
          antennaLocations[lines[i][j]] = [];
        }
        antennaLocations[lines[i][j]].push([i, j]);
      }
    }
  }
  return antennaLocations;
}

function isWithinGrid(node, hmax, vmax) {
  return node[0] >= 0 && node[0] < hmax && node[1] >= 0 && node[1] < vmax;
}

function removeDuplicates(nodes) {
  return Array.from(new Set(nodes.map(JSON.stringify)), JSON.parse);
}

function parseInput(input) {
  const grid = input.trim().split('\r\n');
  const GRID_H = grid[0].length;
  const GRID_V = grid.length;
  const antennaLocations = getAntennaLocations(grid);

  return { GRID_H, GRID_V, antennaLocations };
}

function part1(input) {
  const { GRID_H, GRID_V, antennaLocations } = parseInput(input);

  const allAntinodes = [];
  for (const [_, locations] of Object.entries(antennaLocations)) {
    allAntinodes.push(...findAntinodes(locations));
  }

  return removeDuplicates(allAntinodes)
    .filter((node) => isWithinGrid(node, GRID_H, GRID_V))
    .length;
}

function part2(input) {
  const { GRID_H, GRID_V, antennaLocations } = parseInput(input);

  const allAntinodes = [];
  for (const [_, locations] of Object.entries(antennaLocations)) {
    allAntinodes.push(...findAntinodesForLocations(locations, GRID_H, GRID_V));
  }

  return removeDuplicates(allAntinodes).length;
}

function findAntinodesForLocations(locations, GRID_H, GRID_V) {
  if (locations.length < 2) {
    return [];
  }

  const allAntinodes = [];
  for (let i = 0; i < locations.length; i++) {
    for (let j = 0; j < locations.length; j++) {
      const l1 = locations[i];
      const l2 = locations[j];

      allAntinodes.push(l1);
      allAntinodes.push(l2);

      if (l1[0] === l2[0] && l1[1] === l2[1]) {
        continue;
      }

      let curr = l1;
      let next = l2;

      while (true) {
        const antinode = findAntinode(next, curr);
        if (!isWithinGrid(antinode, GRID_H, GRID_V)) {
          break;
        }

        allAntinodes.push(antinode);

        curr = next;
        next = antinode;
      }
    }
  }

  return allAntinodes;
}

const testInput = fs.readFileSync('test.txt', 'utf8');
const actualInput = fs.readFileSync('input.txt', 'utf8');

console.log('Part 1 (test):', part1(testInput));
console.log('Part 1 (actual):', part1(actualInput));
console.log('Part 2 (test):', part2(testInput));
console.log('Part 2 (actual):', part2(actualInput));
