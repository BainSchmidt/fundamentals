for (int, a = 1; a <= 100; a++) {
        if (a % 5 == 0 && a % 12 == 0) {
            println(a / 5);
            println(a / 12);
        } else if (a % 5 == 0) {
            println(a / 5);
        } else if (a % 12 == 0) {
            println(a / 12);

        } else {
            println(a);
        }
    }