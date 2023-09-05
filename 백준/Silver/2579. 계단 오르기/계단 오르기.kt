import kotlin.math.max

fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.`out`.bufferedWriter()

    val input = br.readLine().toInt()
    val dp = IntArray(input + 1) { 0 }

    val step = mutableListOf<Int>()
    step.add(0)
    repeat(input) {
        step.add(br.readLine().toInt())
    }

    when (input) {
        0 -> {
            bw.write("${step[0]}")
        }

        1 -> {
            bw.write("${step[1]}")
        }

        2 -> {
            bw.write("${step[1] + step[2]}")
        }

        else -> {
            dp[1] = step[1]
            dp[2] = step[1] + step[2]

            for (i in 3..input) {
                dp[i] = max(step[i] + dp[i - 2], step[i] + step[i - 1] + dp[i - 3])
            }
            bw.write("${dp[input]}")
        }
    }

    bw.close()
}