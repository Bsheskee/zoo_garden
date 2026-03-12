class FeedingSchedule:

    def __init__(self, time, food):
        self.time = time
        self.food = food

    def __str__(self):
        return f"Feed at {self.time}: {self.food}"