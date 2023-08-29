import java.util.Scanner

fun main() {
    val scanner = Scanner(System.`in`)

    while (true) {
        val a = scanner.nextInt()
        val b = scanner.nextInt()

        if (a == 0 && b == 0) {
            break
        } else {
            println(a + b)
        }
    }
}
