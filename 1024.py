class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips = sorted(clips)
        counter = 0
        filteredClips = []

        if clips[-1][1] < time:
            return -1

        for i in range(0, (len(clips) - 1)):
            if (clips[i][0]) != (clips[i+1][0]):
                filteredClips.append(clips[i])
        filteredClips.append(clips[-1])
