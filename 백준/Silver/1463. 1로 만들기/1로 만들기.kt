import kotlin.math.min

fun main() {
    val br = System.`in`.bufferedReader()
    val input = br.readLine().toInt()
    val dp = Array(input + 1) { 0 }

    for (i in 2..input) {
        dp[i] = dp[i - 1] + 1
        if (i % 2 == 0) dp[i] = min(dp[i], dp[i / 2] + 1)
        if (i % 3 == 0) dp[i] = min(dp[i], dp[i / 3] + 1)
    }
    print(dp[input])
}
