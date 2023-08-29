import java.io.BufferedReader
import java.io.BufferedWriter
import java.util.LinkedList

private fun BufferedReader.readListWithoutBlank() = this.readLine().map { it.toString().toInt() }
private fun BufferedReader.readList() = this.readLine().split(" ").map { it.toInt() }

fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()

    val (N, M) = br.readList()

    val graph = Array(N + 1) { mutableListOf<Int>() }
    for (i in 1..N) {
        graph[i].addAll(listOf(0) + br.readListWithoutBlank())
    }

    val visited = hashMapOf<Vertex, Boolean>()
    val distance = hashMapOf<Vertex, Int>()

    for (i in 1..N) {
        for (j in 1..M) {
            visited[Vertex(i, j)] = false
            distance[Vertex(i, j)] = 1
        }
    }

    bfs(
        n = N,
        m = M,
        v = Vertex(1, 1),
        graph = graph,
        visited = visited,
        distance = distance
    )
    bw.write("${distance[Vertex(N, M)]}")

    bw.close()
}

private fun bfs(
    n: Int,
    m: Int,
    v: Vertex,
    graph: Array<MutableList<Int>>,
    visited: HashMap<Vertex, Boolean>,
    distance: HashMap<Vertex, Int>
) {
    val dx = arrayListOf(-1, 1, 0, 0)
    val dy = arrayListOf(0, 0, -1, 1)

    val queue = LinkedList<Vertex>()
    queue.offer(v)
    while (!queue.isEmpty()) {
        val currentNode = queue.poll()
        for (i in 0..3) {
            val nx = dx[i] + currentNode.x
            val ny = dy[i] + currentNode.y
            val nextNode = Vertex(nx, ny)
            if (nx <= 0 || nx > n || ny <= 0 || ny > m) {
                continue
            }
            if (graph[nx][ny] == 0) {
                continue
            }
            if (graph[nx][ny] == 1 && visited[nextNode] == false) {
                visited[nextNode] = true
                distance[nextNode] = distance[currentNode]!! + 1
                queue.offer(nextNode)
            }
        }
    }
}

data class Vertex(
    val x: Int,
    val y: Int
)