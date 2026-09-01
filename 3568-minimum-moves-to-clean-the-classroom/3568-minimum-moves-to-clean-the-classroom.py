from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        start = None
        litter_id = {}
        litter_count = 0

        # Find start and assign each litter a bit index
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = litter_count
                    litter_count += 1

        # Mask when all litter has been collected
        all_collected = (1 << litter_count) - 1

        if all_collected == 0:
            return 0

        sr, sc = start

        # (row, col, collected_mask, remaining_energy)
        q = deque([(sr, sc, 0, energy)])

        # best[r][c][mask] = maximum energy we've had
        # when reaching this position with this mask
        best = [
            [[-1] * (1 << litter_count) for _ in range(n)]
            for _ in range(m)
        ]

        best[sr][sc][0] = energy

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        moves = 0

        while q:
            # Process one BFS level = one move
            for _ in range(len(q)):
                r, c, mask, curr_energy = q.popleft()

                # A better version of this state was already found
                if curr_energy < best[r][c][mask]:
                    continue

                # All litter collected
                if mask == all_collected:
                    return moves

                # Can't move if we have no energy
                if curr_energy == 0:
                    continue

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Check boundaries
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    # Can't walk through obstacles
                    if classroom[nr][nc] == 'X':
                        continue

                    new_energy = curr_energy - 1
                    new_mask = mask

                    # Collect litter
                    if classroom[nr][nc] == 'L':
                        idx = litter_id[(nr, nc)]
                        new_mask |= (1 << idx)

                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    # Only keep this state if it gives us more energy
                    if new_energy > best[nr][nc][new_mask]:
                        best[nr][nc][new_mask] = new_energy
                        q.append((nr, nc, new_mask, new_energy))

            moves += 1

        return -1