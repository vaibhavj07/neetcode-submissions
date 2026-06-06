class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        pair.sort(reverse=True)   # sort by position from closest to target

        fleets = []

        for pos, spd in pair:
            time = (target - pos) / spd

            # if this car catches up to previous fleet,
            # it becomes part of that fleet
            if fleets and time <= fleets[-1]:
                continue

            fleets.append(time)

        return len(fleets)