import kotlin.math.max

fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.`out`.bufferedWriter()

    val T = br.readLine().toInt()

    repeat(T) {
        val N = br.readLine().toInt()
        val dp = Array(2) { IntArray(N) }
        val arr = Array(2) { mutableListOf<Int>() }
        for (i in 0..1) {
            arr[i].addAll(br.readLine().split(" ").map { it.toInt() })
        }
        if (N >= 1) {
            dp[0][0] = arr[0][0]
            dp[1][0] = arr[1][0]
        }
        if (N >= 2) {
            dp[0][1] = dp[1][0] + arr[0][1]
            dp[1][1] = dp[0][0] + arr[1][1]
        }
        for (i in 2 until N) {
            dp[0][i] = max(arr[0][i] + dp[1][i - 1], arr[0][i] + dp[1][i - 2])
            dp[1][i] = max(arr[1][i] + dp[0][i - 1], arr[1][i] + dp[0][i - 2])
        }

        val ans = max(dp[0][N - 1], dp[1][N - 1])
        bw.write("$ans \n")
    }
    bw.close()

}