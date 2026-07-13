class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        comb = list(zip(position, speed))
        comb.sort(reverse = True)
        fleet = []
        for ele in comb:
            time_to_complete = (target-ele[0])/ele[1]
            fleet.append(time_to_complete)
            if len(fleet)>=2:
                if fleet[-2]>=fleet[-1]:
                    fleet.pop()
        return len(fleet)       