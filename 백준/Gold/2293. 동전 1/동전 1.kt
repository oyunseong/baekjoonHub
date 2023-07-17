
fun main() = with(System.`in`.bufferedReader()) {
    val (n, k) = readLine().split(" ").map { it.toInt() }
    val dp = IntArray(k + 1)
    dp[0] = 1
    val coins = IntArray(n)
    for (i in 0 until n) {
        coins[i] = readLine().toInt()
    }

    coins.forEach { c ->
        for (i in c..k) {
            dp[i] = dp[i] + dp[i - c]
        }
    }
    print(dp[k])
}
