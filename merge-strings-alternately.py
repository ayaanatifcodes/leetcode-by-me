class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newstring = ""
        for i in range(min(len(word1), len(word2))):
            newstring += word1[i]
            newstring += word2[i]
        if len(word1) > len(word2):
            newstring += word1[len(word2):]
        else:
           newstring += word2[len(word1):]
        return newstring

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
