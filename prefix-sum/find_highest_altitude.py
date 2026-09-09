class Solution:
    def largestAltitude(self, gain):
        current_altitude = 0
        max_altitude = 0
        
        for change in gain:
            current_altitude += change
            max_altitude = max(max_altitude, current_altitude)
        
        return max_altitude