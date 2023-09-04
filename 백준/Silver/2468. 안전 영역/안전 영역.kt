import java.util.*
import kotlin.collections.HashMap

fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.`out`.bufferedWriter()

    val input = br.readLine()
    val N = input.toInt()   // N : 행과 열의 개수
    var threshold: Int   // 잠기는 높이
    val graph = Array(N + 1) { mutableListOf<Int>() }
    val visited = HashMap<Vertex, Boolean>()
    var waterHigh = 0

    for (i in 0..N) {
        graph[0].add(0)
    }
    // 그래프 입력
    for (i in 1..N) {
        graph[i].addAll(listOf(0) + br.readLine().split(" ").map {
            if (it.toInt() > waterHigh) {
                waterHigh = it.toInt()
            }
            it.toInt()
        })
    }

    var max = 1
    for (i in 1 until waterHigh) {

        // NxM 배열 방문상태 초기화
        for (x in 1..N) {
            for (y in 1..N) {
                visited[Vertex(x, y)] = false
            }
        }
        var cnt = 0

        for (n in 1..N) {
            for (m in 1..N) {
                if (graph[n][m] <= i) continue
                if (visited[Vertex(n, m)] == true) continue
                bfs(
                    N = N,
                    v = Vertex(n, m),
                    threshold = i,
                    visited = visited,
                    graph = graph
                )
                cnt += 1
            }
        }
        if (max < cnt) max = cnt
    }

    bw.write("$max")
    bw.close()
}

private fun bfs(
    N: Int,
    v: Vertex,
    threshold: Int,
    visited: HashMap<Vertex, Boolean>,
    graph: Array<MutableList<Int>>,
) {
    val dx = listOf(-1, 1, 0, 0)
    val dy = listOf(0, 0, -1, 1)
    val queue = LinkedList<Vertex>()

    queue.offer(v)
    visited[v] = true

    while (!queue.isEmpty()) {
        val currentNode = queue.poll()
        for (i in 0..3) {
            val nx = dx[i] + currentNode.x
            val ny = dy[i] + currentNode.y
            val nextNode = Vertex(nx, ny)
            if (nx <= 0 || nx > N || ny <= 0 || ny > N) continue
            if (visited[nextNode] == true || graph[nx][ny] <= threshold) continue
            queue.offer(nextNode)
            visited[nextNode] = true
        }
    }
}

data class Vertex(
    val x: Int,
    val y: Int
)
