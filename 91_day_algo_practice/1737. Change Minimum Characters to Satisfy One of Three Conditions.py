class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        # Initialize counters for each letter in the alphabet
        counter1, counter2 = [0] * 26, [0] * 26

        # Count occurrences of each letter in string 'a'
        for c in a:
            counter1[ord(c) - ord("a")] += 1

        # Count occurrences of each letter in string 'b'
        for c in b:
            counter2[ord(c) - ord("a")] += 1

        # Calculate minimum operations for condition 1
        way1 = min(sum(counter1[i:]) + sum(counter2[:i]) for i in range(1, 26))

        # Calculate minimum operations for condition 2
        way2 = min(sum(counter2[i:]) + sum(counter1[:i]) for i in range(1, 26))

        # Calculate minimum operations for condition 3
        way3 = min(len(a) + len(b) - counter1[i] - counter2[i] for i in range(26))

        # Return the overall minimum operations among the three conditions
        return min(way1, way2, way3)
