with open("beyond the wall of sleep.txt","r") as file:
    beyond_the_wall = file.read()
beyond_the_wall = "".join((char if char.isalpha() else " ") for char in beyond_the_wall).split()
for i in range(len(beyond_the_wall)):
    beyond_the_wall[i] = beyond_the_wall[i].lower()
beyond_the_wall = set(beyond_the_wall)
with open("pride and projection.txt","r") as file:
    pride_and = file.read()
pride_and = "".join((char if char.isalpha() else " ") for char in pride_and).split()
for i in range(len(pride_and)):
    pride_and[i] = pride_and[i].lower()
pride_and = set(pride_and)
stop_words = {"ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out", "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into", "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him", "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were", "her", "more", "himself", "this", "down", "should", "our", "their", "while", "above", "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them", "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then", "that", "because", "what", "over", "why", "so", "can", "did", "not", "now", "under", "he", "you", "herself", "has", "just", "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom", "t", "being", "if", "theirs", "my", "against", "a", "by", "doing", "it", "how", "further", "was", "here", "than"}
common = pride_and.intersection(beyond_the_wall).difference(stop_words)
print("number of common words : ",len(common))
#if you want to print common words
#print(common)