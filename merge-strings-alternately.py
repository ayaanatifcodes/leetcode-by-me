class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string = ""
        min_length = min(len(word1), len(word2))
        for i in range(min_length):
            string += word1[i]
            string += word2[i]
        if len(word1) > len(word2):
            string += word1[min_length:]
        else:
            string += word2[min_length:]
        return string

# Javascript Approach        
# /**
# * @param {string} word1
# * @param {string} word2
# * @return {string}
# */
# var mergeAlternately = function(word1, word2) {
#   let merged_Arr = []
#   for(let i = 0; i < word1.length || i < word2.length; i++) {
#       merged_Arr.push(word1[i], word2[i])
#   }
#   return merged_Arr.join('')
# }
