class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """


        
        strs = ["flower","flow","flight"]
        matchedletters = ""
        # first for loop is going through the List of strings
        for words in strs:
            print(words)
        # the inside for loop has to go through each of the characters
        # but we want the front letters, not the ones in the back, since its a prefex not suffix
            for char in enumerate(words):
                print(char)

            # while it's going thro the characters it needs to compare to see if
            # chracters are matching in the other strings
           
            # if there is a match, add it to the matchedletters variable