'''
A social media company is trying to monitor activity on their site by analyzing the number of tweets that occur in select periods of time. These periods can be partitioned into smaller time chunks based on a certain frequency (every minute, hour, or day).

For example, the period [10, 10000] (in seconds) would be partitioned into the following time chunks with these frequencies:

Every minute (60-second chunks): [10,69], [70,129], [130,189], ..., [9970,10000]
Every hour (3600-second chunks): [10,3609], [3610,7209], [7210,10000]
Every day (86400-second chunks): [10,10000]
Notice that the last chunk may be shorter than the specified frequency's chunk size and will always end with the end time of the period (10000 in the above example).

Design and implement an API to help the company with their analysis.

Implement the TweetCounts class:

TweetCounts() Initializes the TweetCounts object.
void recordTweet(String tweetName, int time) Stores the tweetName at the recorded time (in seconds).
List<Integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime) Returns a list of integers representing the number of tweets with tweetName in each time chunk for the given period of time [startTime, endTime] (in seconds) and frequency freq.
freq is one of "minute", "hour", or "day" representing a frequency of every minute, hour, or day respectively.
 

Example:

Input
["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
[[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]

Output
[null,null,null,null,[2],[2,1],null,[4]]

Explanation
TweetCounts tweetCounts = new TweetCounts();
tweetCounts.recordTweet("tweet3", 0);                              // New tweet "tweet3" at time 0
tweetCounts.recordTweet("tweet3", 60);                             // New tweet "tweet3" at time 60
tweetCounts.recordTweet("tweet3", 10);                             // New tweet "tweet3" at time 10
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59); // return [2]; chunk [0,59] had 2 tweets
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60); // return [2,1]; chunk [0,59] had 2 tweets, chunk [60,60] had 1 tweet
tweetCounts.recordTweet("tweet3", 120);                            // New tweet "tweet3" at time 120
tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210);  // return [4]; chunk [0,210] had 4 tweets

Input:
Output:


Precondition:
no int overflow
tweetname only ASCII words
n = number of inputs
n >= 0
dup can be added to one time point for each tweet

Postcondition:
Change in place
get should return 

C1: cannot get, return []
C2: get and return one chunk
C3: get and return mult chunk

Algo
Hashmap + binary search
Runtime: 
Record: O(n)
Get: O(n)
Space: O(n)
'''
class TweetCounts:

    def __init__(self):
        self.tweets = defaultDict(SortedList)
        self.freq_mapping = {"minute": 60, "hour": 3600, "day":86400}
        

    def recordTweet(self, Tweetname, time):
        """
        :type tweetName: str
        :type time: int
        :rtype: None
        """
        if Tweetname not in self.tweets:
            self.tweets[Tweetname].append(time)
        else:
            idx = bisect.bisect(self.tweets[Tweetname], time)
            self.tweets[Tweetname].insert(idx, time)
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        freq_number = self.freq_mapping[freq]
        target = self.tweets[tweetName]
        result = [0] * ((endTime - startTime) // freq_number + 1)
        start_index = bisect.bisect_left(target, startTime)
        end_index = bisect.bisect_right(target, endTime)

        for i in range(start_index, end_index):
            target_block = (target[i] - startTime) // freq_number
            result[target_block] += 1
        return result 

        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)