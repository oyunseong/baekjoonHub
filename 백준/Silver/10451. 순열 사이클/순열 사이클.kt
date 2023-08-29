import java.io.BufferedReader
import java.util.*

private fun BufferedReader.readInt() = this.readLine().toInt()
private fun BufferedReader.readListToInt() = this.readLine().split(" ").map { it.toInt() }

fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()
    val t = br.readInt()

    repeat(t) {
        val n = br.readInt()
        val permutation = br.readListToInt()
        val graph: HashMap<Int, Int> = hashMapOf()
        val visited: HashMap<Int, Boolean> = hashMapOf()
        for (i in 1..n) {
            graph[i] = permutation[i-1]
            visited[i] = false
        }

        var count = 0
        for (i in 1..n) {
            if (!visited[i]!!) {
                bfs(
                    v = i,
                    graph = graph,
                    visited = visited
                )
                count += 1
            }
        }

        bw.write("$count")
        bw.write("\n")
    }
    bw.close()
}

private fun bfs(
    v: Int,
    graph: HashMap<Int, Int>,
    visited: HashMap<Int, Boolean>,
) {
    val queue = LinkedList<Int>()
    queue.offer(v)

    while (!queue.isEmpty()) {
        val currentNode = queue.poll()
        if (!visited[currentNode]!!) {
            val nextNode = graph[currentNode]
            visited[currentNode!!] = true
            queue.offer(nextNode)
        }
    }
}
