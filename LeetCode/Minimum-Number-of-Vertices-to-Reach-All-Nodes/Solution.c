/**
 * Return an array of size* returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findSmallestSetOfVertices(int n, int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    int* indegree = (int*)calloc(n, sizeof(int));

    // Count indegree for each node
    for (int i = 0; i < edgesSize; i++) {
        int to = edges[i][1];
        indegree[to] = 1;   // Mark that this node has an incoming edge
    }

    // Count nodes with indegree = 0
    int* result = (int*)malloc(n * sizeof(int));
    int idx = 0;

    for (int i = 0; i < n; i++) {
        if (indegree[i] == 0) {
            result[idx++] = i;
        }
    }

    free(indegree);

    *returnSize = idx;
    return result;
}
