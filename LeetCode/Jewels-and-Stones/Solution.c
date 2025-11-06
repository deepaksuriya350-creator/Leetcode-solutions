int numJewelsInStones(char* jewels, char* stones) {
    int freq[128] = {0};
    int count = 0;

    for (int i = 0; jewels[i]; i++)
        freq[(int)jewels[i]] = 1;

    for (int i = 0; stones[i]; i++)
        if (freq[(int)stones[i]])
            count++;

    return count;
}
