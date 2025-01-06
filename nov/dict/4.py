def anagram():
    t = int(input(" size of words ="))

    for _ in range(t):
        word1 = input().strip()
        word2 = input().strip()

        if sorted(word1) == sorted(word2):
            print("True")
        else:
            print("False")



anagram()












